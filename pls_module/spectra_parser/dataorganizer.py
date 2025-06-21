import pandas as pd

class DataOrganizer:
    """Class for organizing data

    :param file_name: file path of .csv file
    """
    def __init__(self, file_name):
        self.file_path = file_name
        self.raw_df = None
        self.trimmed_df = None
        self.wavenumbers_list = None
        self.absorbance_list = None
        self.y_block = None

    def open_file(self):
        """ Opens a .csv file and convert it into a pandas dataframe
        """
        self.raw_df = pd.read_csv(self.file_path)

    def org_data(self):
        """ Organizes data, ready for further transformation or modelling

        :return: None, message for missing data
        :rtype: None, str
        """
        if not all(self.raw_df):
            return "no data found"
        else:
            self.trimmed_df = self.raw_df.set_index("Label").iloc[:, 7:2081].sort_index()
            self.trimmed_df.columns = [round(float(wn), 2) for wn in self.trimmed_df.columns.astype(float)]
            self.y_block = self.raw_df.set_index("Label").iloc[:,2081:2084].sort_index()
            
            # self.wavenumbers_list = self.trimmed_df.columns.to_list() # list of wavenumbers used
            #self.absorbance_list = self.trimmed_df.iloc[0, :].to_list() # just getting one sample here

    def give_abs(self):
        """ Give the absorbance values of spectral data

        :return: list of absorbance values
        :rtype: list
        """
        if not all(self.absorbance_list):
            return "no data found"
        return self.absorbance_list

    def give_wn(self):
        """ Give the wavenumber values of spectral data

        :return: list of wavenumber values
        :rtype: list
        """
        if not all(self.wavenumbers_list):
            return "no data found"
        return self.wavenumbers_list

    def give_xblock(self):
        """ Give the organized values of the variable block

        :return: organized x-block
        :rtype: dataframe
        """
        if not all(self.trimmed_df):
            return "no data found"
        return self.trimmed_df

    def give_yblock(self, mode="normal"):
        """ Give the organized values of the response block

        :return: organized yblock
        :rtype: dataframe
        """
        if mode == "test":
            return [1]*25 + [5]*25 + [0.2]*25 + [100]*25 # len(test_y) this is sample y-block data only
        else:
            return self.y_block.sum(1)