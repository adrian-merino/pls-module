from scipy.signal import savgol_filter, find_peaks
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score

class PLSModel:
    def __init__(self, data_df):
        self.raw_df = data_df
        
    def apply_sg(self, data_df, pts=17, poly_order=2, deriv=2):
        df_sg = savgol_filter(data_df, pts, poly_order, deriv)
        return df_sg
    
    def create_model(self, X, y, n_comp):
        # Define PLS object
        pls = PLSRegression(n_components=n_comp)

        # Cross-validation
        y_cv = cross_val_predict(pls, X, y, cv=10)

        # Calculate scores
        r2 = r2_score(y, y_cv)
        mse = mean_squared_error(y, y_cv)
        #rpd = y.std()/np.sqrt(mse)

        return (y_cv, r2, mse)