from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
    
class ModelCreator:
    def load_data(self, x, y):
        self.working_xblock = x
        self.working_yblock = y
        
    def create_pls_model(self, n_comp=1):
        # Autoscale Y-block
        autoscaler = StandardScaler()
        y_autoscaled = autoscaler.fit_transform(self.working_yblock.to_numpy().reshape(-1, 1))
        
        # Define PLS object
        pls = PLSRegression(n_components=n_comp)
        pls.fit(self.working_xblock, y_autoscaled)
        
        # Calibration Scores
        y_cal = pls.predict(self.working_xblock)
        r2_cal_sci = r2_score(y_cal.ravel(), y_autoscaled)
        r2_cal_sol, _ = pearsonr(y_autoscaled.ravel(), y_cal.ravel())
        mse_cal = mean_squared_error(y_autoscaled, y_cal)
        
        # Cross-validation Scores
        y_cv = cross_val_predict(pls, self.working_xblock, y_autoscaled, cv=3)
        r2_cv_sci = r2_score(self.working_yblock.to_numpy(), y_cv.ravel())
        r2_cv_sol, _ = pearsonr(self.working_yblock.to_numpy().ravel(), y_cv.ravel())
        mse_cv = mean_squared_error(y_autoscaled, y_cv)
    
        return (
            round(r2_cal_sci,2), 
            round(r2_cv_sci,2), 
            round(float(r2_cal_sol)**2,4), 
            round(float(r2_cv_sol)**2,4), 
            round(mse_cal,4), 
            round(mse_cv,4),
        )