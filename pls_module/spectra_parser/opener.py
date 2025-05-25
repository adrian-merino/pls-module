import pandas as pd

def open_file(file_path):
    df = pd.read_csv(file_path)
    return df