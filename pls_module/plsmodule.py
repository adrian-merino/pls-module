from .spectra_parser import DataManager, DataSelector, DataOrganizer, PLSModel
from .modeler import ModelCreator
from .preprocessing import Preprocessor

from itertools import combinations, permutations

class PLSModeler:
    def __init__ (self, file_path):
        self.pls_modeler = PLSModel(file_path)
        self.data_manager = DataManager(file_path)
        self.data_x = self.data_manager.open_file(1)
        self.data_y = [1]*25 + [5]*25 + [0.2]*25 + [100]*25
        
    def give_model(self, n_comp=1):
        return self.pls_modeler.create_model(
            self.data_x,
            self.data_y,
            n_comp
        )
    
class IPLSModeler:
    """ Class for filtering data for samples or wavenumbers to be removed

    :param file_name: file path of .csv file
    """
    def __init__ (self, file_path=0):
        self.file_path = file_path

        self.data_organizer = DataOrganizer(self.file_path)
        self.data_filterer = DataSelector()
        self.preprocessor = Preprocessor()
        self.model_creator = ModelCreator()
        
        self.org_xblock = None
        self.org_yblock = None

        self.working_xblock = None
        self.working_yblock = None

        # settings
        self.pts_list = []
        self.regions_list = []
        self.preproc_list = []

        # IPLS results
        self.settings_list = []
        self.results_list = []

    def organize_data(self):
        """ Organizes data read for further transformation and modelling"""
        self.data_organizer.open_file()
        self.data_organizer.org_data()
        self.org_xblock = self.data_organizer.give_xblock()
        self.org_yblock = self.data_organizer.give_yblock()
        self.data_filterer.load_data(self.org_xblock, self.org_yblock)
        self.working_xblock = self.org_xblock
        self.working_yblock = self.org_yblock
        

    def do_preprocessing(self, preproc_list):
        """ Func for triggering preprocessing of data

        :param preproc_list: list of preprocessing methods for transforming data set, list
        """
        if preproc_list:
            self.preproc_list = preproc_list
            self.preprocessor.load_data(self.working_xblock)
            self.working_xblock = self.preprocessor.preprocess(preproc_list)

    # for setting up lists
    def pick_preproc(self, picked_preproc):
        """ Func for accepting preprocessing methods to be used

        :param picked_preproc: list of preprocessing methods to be used, list
        """
        self.preproc_list = picked_preproc
        return
        
    def select_region(self, region_list):
        """ Func for accepting wavenumber regions to be used

        :param region_list: list of lists containing start and end wavenumbers of regions of interest, list
        """
        if region_list:
            self.regions_list = region_list
            self.data_filterer.pick_regions(self.regions_list)
            self.working_xblock = self.data_filterer.give_xblock()
    
    def remove_point(self, points_list):
        """ Func for accepting samples to be removed

        :param points_list: list of samples names to be excluded, list
        """
        if points_list:
            self.pts_list = points_list
            self.data_filterer.remove_samples(self.pts_list, True)
            self.working_xblock = self.data_filterer.give_xblock()
            self.working_yblock = self.data_filterer.give_yblock()

    # main funcs
    def get_ipls_settings(self):
        """ Func for creating a list of all possible settings for modelling

        :return: list of all possible configurations of wavenumbers, preproc methods, and samples for modelling
        :rtype: list
        """
        # Check all combinations of removed points
        for pt_num in range (0, len(self.pts_list)+1):
            for pt_comb in combinations(self.pts_list, pt_num):
            
                for region_num in range(0, len(self.regions_list)+1):
                    for region_comb in combinations(self.regions_list, region_num):
    
                        for preproc_num in range(0, len(self.preproc_list)+1):
                            for preproc_comb in permutations(self.preproc_list, preproc_num):
                                if all([region_comb, preproc_comb]):
                                    self.settings_list.append([pt_comb, region_comb, preproc_comb])
        return self.settings_list

    def get_ipls_results(self):
        """ Func for creating PLS models for each configuration in the settings list

        :return: list containing performance metrics of each created model, along with its setting
        :rtype: list
        """
        for settings in self.settings_list:
            self.organize_data()
            self.select_region(settings[1])
            
            self.remove_point(settings[0])
            self.do_preprocessing(settings[2])
            
            self.model_creator.load_data(self.working_xblock, self.working_yblock)
            results = (self.model_creator.create_pls_model(), settings)
            
            print(results)
            self.results_list.append(results)
        return self.results_list