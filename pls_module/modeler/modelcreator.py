from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score

class ModelCreator:
    def load_data(self, x, y):
        self.working_xblock = x
        self.working_yblock = y
        
    def create_pls_model(self, n_comp=6):
        # Define PLS object
        pls = PLSRegression(n_components=n_comp)

        # Cross-validation
        y_cv = cross_val_predict(pls, self.working_xblock, self.working_yblock, cv=10)
        # Calculate scores
        r2 = r2_score(self.working_yblock, y_cv)
        mse = mean_squared_error(self.working_yblock, y_cv)
    
        return r2 # (r2, mse)