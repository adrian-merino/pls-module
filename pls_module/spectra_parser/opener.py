import pandas as pd

class DataManager:
    """ Class for opening files containing data for modelling"""
    def __init__(self, filepath):
        self.filepath = filepath
    
    def open_file(self, trim=0):
        """ Opens a .csv file into a dataframe

        :param trim: indicator if data is to be trimmed, bool
        :return: dataframe containing parsed data
        :rtype: dataframe
        """
        df = pd.read_csv(self.filepath)

        if trim:
            return df.iloc[:, 9:]
            # df = trimmed_df.iloc[0, :].to_list()
        return df