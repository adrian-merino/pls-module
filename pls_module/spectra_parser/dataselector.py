from pandas import pd

class DataSelector:
    def __init__(self):
        self.working_xblock = None
        self.working_yblock = None

    def load_data(self, xblock, yblock):
        self.working_xblock = xblock
        self.working_yblock = yblock

    def remove_samples(self, samples_list, touch_y=False):
        self.working_xblock = self.working_xblock.drop(list(samples_list))
        if touch_y:
            self.working_yblock = self.working_yblock.drop(list(samples_list))
    
    def pick_regions(self, regions_list):
        df_list = []
        for region in regions_list:
            df_list.append(self.working_xblock.loc[:, region[0]:region[1]])
        self.working_xblock = pd.concat(df_list, axis=1)

    def give_xblock(self):
        return self.working_xblock

    def give_yblock(self):
        return self.working_yblock