import pandas as pd

class DataManager:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def open_file(self, trim=0):
        df = pd.read_csv(self.filepath)

        if trim:
            return df.iloc[:, 9:]
            # df = trimmed_df.iloc[0, :].to_list()
        return df