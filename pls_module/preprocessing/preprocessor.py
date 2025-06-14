import numpy as np
import pybaselines as bl

from scipy import sparse
from scipy.signal import savgol_filter, find_peaks
from scipy.sparse.linalg import spsolve
from scipy.linalg import cholesky

class Preprocessor:
    def __init__(self):
        self.working_data = None

    def load_data(self, data):
        self.working_data = data

    def give_xblock(self):
        return self.working_data

    # used for dataframes
    def apply_sg(self, smooth_pts=15, poly_order=2, deriv_order=2):
        return self.working_data.iloc[:,1:].apply(
            lambda x: savgol_filter(np.array(x), smooth_pts, poly_order, deriv_order), #double check this one
            axis=1, 
            result_type='broadcast',
        )

    def apply_snv(self):
        # return raw_data.sub(raw_data.mean(axis=1), axis=0).div(raw_data.std(axis=1, ddof=0), axis=0)
        sub_by_mean = self.working_data.sub(self.working_data.mean(1), axis=0)
        self.working_data = sub_by_mean.div(self.working_data.std(1), axis=0)


    def apply_wlsb(self):
        corr = bl.Baseline()
        
        def test(x): 
            return  np.array(x) - corr.loess(
                np.array(x), 
                # poly_order=5, 
                # max_iter=100, 
                # scale=2.1,
                conserve_memory=False,
            )[0]
        self.working_data =  self.working_data.iloc[:,1:].apply(
            test,
            axis=1, 
            result_type='broadcast',
        )

    def apply_wlsb2(self, y, lam=1e4, ratio=0.05, itermax=100):
        N = len(y)
        D = sparse.eye(N, format='csc')
        D = D[1:] - D[:-1]  # numpy.diff( ,2) does not work with sparse matrix. This is a workaround.
        D = D[1:] - D[:-1]
        H = lam * D.T * D
        w = np.ones(N)
        for i in range(itermax):
            W = sparse.diags(w, 0, shape=(N, N))
            WH = sparse.csc_matrix(W + H)
            C = sparse.csc_matrix(cholesky(WH.todense()))
            z = spsolve(C, spsolve(C.T, w * y))
            d = y - z
            dn = d[d < 0]
            m = np.mean(dn)
            s = np.std(dn)
            wt = 1. / (1 + np.exp(2 * (d - (2 * s - m)) / s))
            if np.linalg.norm(w - wt) / np.linalg.norm(w) < ratio:
                break
            w = wt
        return z

    def apply_wlsb3(self, y, lam=10, p=0.1, niter=10):
        L = len(y)
        D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
        w = np.ones(L)
        for i in range(niter):
            W = sparse.spdiags(w, 0, L, L)
            Z = W + lam * D.dot(D.transpose())
            z = spsolve(Z, w*y)
            w = p * (y > z) + (1-p) * (y < z)
        return z

    def apply_meancenter(self):
        self.working_data = self.working_data - self.working_data.mean()
    
    def preprocess(self, preprocess_list):
        for technique in preprocess_list:
            if technique == "SG":
                self.apply_sg()
            if technique == "WLSB":
                self.apply_wlsb()
            if technique == "SNV":
                self.apply_snv()
            if technique == "MC":
                self.apply_meancenter()

        return self.working_data