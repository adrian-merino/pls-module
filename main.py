import warnings

from pls_module import IPLSModeler

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
    list_pls_models_test("tests/test_data.csv", True)