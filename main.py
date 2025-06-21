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
    results = a.get_ipls_results()

    max_val = max([res[0] for res in results])
    best_settings = results[[res[0] for res in results].index(max_val)][1]
    print(f"max r2 is {max_val} with settings of {best_settings}")

if __name__ == "__main__":
    list_pls_models_test("tests/test_data.csv", True)