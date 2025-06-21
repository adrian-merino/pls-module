from pls_module import PLSModeler, IPLSModeler

import warnings

def create_pls_model():
    pls_modeler = PLSModeler("test2.csv")
    return pls_modeler.give_model()

def list_pls_models_test(file_path, disable_warnings=False):
    if disable_warnings:
        warnings.filterwarnings('ignore')

    a = IPLSModeler(file_path)
    a.organize_data()

    a.select_region([[5300, 4700], [6600, 6390]])
    a.pick_preproc(["SG", "SNV", "MC",])

    a.get_ipls_settings()
    a.get_ipls_results()

if __name__ == "__main__":
    print(create_pls_model())
    list_pls_models_test("test3.csv", True)