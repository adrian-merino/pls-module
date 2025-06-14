import pandas as pd

class DataOrganizer:
    def __init__(self, file_name):
        self.file_path = file_name
        self.raw_df = None
        self.trimmed_df = None
        self.wavenumbers_list = None
        self.absorbance_list = None
        self.y_block = None

    def open_file(self):
        self.raw_df = pd.read_csv(self.file_path)
        self.raw_df = self.raw_df.loc[self.raw_df['Gum Product'] == 795]

    def org_data(self):
        if not all(self.raw_df):
            return "no data found"
        else:
            
            self.trimmed_df = self.raw_df.set_index("Label").iloc[:, 7:2081].sort_index()
            self.trimmed_df.columns = [round(float(wn), 2) for wn in self.trimmed_df.columns.astype(float)]
            self.y_block = self.raw_df.set_index("Label").iloc[:,2081:2084].sort_index()
            
            self.wavenumbers_list = self.trimmed_df.columns.to_list() # list of wavenumbers used
            self.absorbance_list = self.trimmed_df.iloc[0, :].to_list() # just getting one sample here

    def give_abs(self):
        if not all(self.absorbance_list):
            return "no data found"
        return self.absorbance_list

    def give_wn(self):
        if not all(self.wavenumbers_list):
            return "no data found"
        return self.wavenumbers_list

    def give_xblock(self):
        if not all(self.trimmed_df):
            return "no data found"
        return self.trimmed_df

    def give_yblock(self, mode="normal"):
        if mode == "test":
            return [1]*25 + [5]*25 + [0.2]*25 + [100]*25 # len(test_y) this is sample y-block data only
        else:
            return self.y_block.sum(1)