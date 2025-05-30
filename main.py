from pls_module import PLSModeler

def create_pls_model():
    pls_modeler = PLSModeler("test2.csv")
    return pls_modeler.give_model()

if __name__ == "__main__":
    print(create_pls_model())