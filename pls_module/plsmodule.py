from .spectra_parser import DataManager, PLSModel

class PLSModeler:
    def __init__ (self, file_path):
        self.pls_modeler = PLSModel(file_path)
        self.data_manager = DataManager(file_path)
        self.data_x = self.data_manager.open_file(1)
        self.data_y = [1]*25 + [5]*25 + [0.2]*25 + [100]*25
        
    def give_model(self, n_comp=1):
        return self.pls_modeler.create_model(
            self.data_x,
            self.data_y,
            n_comp
        )