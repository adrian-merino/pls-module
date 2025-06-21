from pandas import pd

class DataSelector:
    """Class for filtering data for samples or wavenumbers to be removed"""
    def __init__(self):
        self.working_xblock = None
        self.working_yblock = None

    def load_data(self, xblock, yblock):
        """ Loads data to DataSelector object

        :param xblock: table of variable values, dataframe
        :param yblock: table of response values, dataframe
        """
        self.working_xblock = xblock
        self.working_yblock = yblock

    def remove_samples(self, samples_list, touch_y=False):
        """ Remove samples from provided list

        :param samples_list: samples to be excluded from the calibration data, list
        :param touch_y: indicator if y-block will have its samples removed as well, bool
        """
        self.working_xblock = self.working_xblock.drop(list(samples_list))
        if touch_y:
            self.working_yblock = self.working_yblock.drop(list(samples_list))
    
    def pick_regions(self, regions_list):
        """ Remove regions of wavenumbers from provided list

        :param regions_list: list containing lists of start and end of wavenumber region to be removed, list
        """
        df_list = []
        for region in regions_list:
            df_list.append(self.working_xblock.loc[:, region[0]:region[1]])
        self.working_xblock = pd.concat(df_list, axis=1)

    def give_xblock(self):
        """ Returns filtered x-block

        :return: x-block
        :rtype: dataframe
        """
        return self.working_xblock

    def give_yblock(self):
        """ Returns filtered y-block

        :return: y-block
        :rtype: dataframe
        """
        return self.working_yblock