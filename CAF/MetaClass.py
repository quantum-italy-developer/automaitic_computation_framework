"""
MetaClass
=========================
Script containing metaclass of referement to design class for calculation and plot

"""
# =============================================================================
# Module attributes
# =============================================================================
# Documentation format
__docformat__ = 'NumPy'
# License type (e.g. 'GPL', 'MIT', 'Proprietary', ...)
__license__ = 'Proprietary'
# Status ('Prototype', 'Development' or 'Pre-production')
__status__ = 'Development'
# Version (0.0.x = 'Prototype', 0.x.x = 'Development', x.x.x = 'Pre-production)
__version__ = '0.1.0'
# Authors (e.g. code writers)
__author__ = ('Antonello Aita <>',
              'Luca Crippa <>',
              'Michele Grossi <>')
# Maintainer
__maintainer__ = ''
# Email of the maintainer
__email__ = ''

# =============================================================================
# Import modules
# =============================================================================
# Import general purpose module(s)
import abc
import datetime
import json
from qiskit import IBMQ
# Import custom module(s)
from CAF import utils

# =============================================================================
# =============================================================================
# Computation MetaClass
# =============================================================================
# =============================================================================
class ComputationClass:
    """
    This metaclass contains the backbone of the computation class .
    It is composed by 3 different elements:

    1) **init** : the constructor function through we collect credential to log on database and IBMQ system

    2) **run** : function designated to gather parameters for each run, then run calculation (on local or remote) and then save the results in the 'final_json' class attribute -- To implement your class --

    3) **save** : function designated to save results on database

    **NB**: Instantiating the class will not require any argoument because an automatic feeding has been implemented
    using a decorator.




    """
    __metaclass__ = abc.ABCMeta

    @utils.configuration_retriever('.')
    def __init__(self,db_credential: dict, ibmq_credential: dict):
        """
        The @utils.configuration_retriever() decorator enable an automatical extraction of the credential from the
        'private_config.json' and set the credential to be used in the other methods in order to connect with db and
        IBMQ system.

        Parameters
        ----------
        db_credential
        ibmq_credential
        """

        # QUANTUM PART
        # =============================================================================
        # Load IBM Q credentials
        self.hub = ibmq_credential['hub']
        self.group = ibmq_credential['group']
        self.project = ibmq_credential['project']
        self.api_key = ibmq_credential['my_api_token']

        # Load IBMQ account
        #self.provider = IBMQ.enable_account(self.api_key)

        # DB PART
        # =============================================================================
        # db user credential import
        self.db_credential = db_credential


        # DATA GATHERING
        # =============================================================================
        # create instance of final json
        self.final_json = {}

        # Initial timestamp
        self.final_json['initial_timestamp'] = str(datetime.datetime.now())

    # =============================================================================
    # Run Function
    # =============================================================================
    @abc.abstractmethod
    def run(self):
        """
        Run function

        This function **must** be implemented in the class you are going to implement

        Returns
        -------

        """
        """Design Run Function"""
        raise NotImplementedError

    # =============================================================================
    # Save Function
    # =============================================================================
    def save(self, db_name:str):
        """
                Save function

                This function save the obtained results presente on the internal json named "final_json" that is populated
                during the perford calculation

                Parameters
                ----------
                db_name: str
                        name of the db created on the cloud instance to collect data

                Returns
                -------

                """

        self.final_json['final_timestamp'] = str(datetime.datetime.now())
        self.final_json['computational_time'] = str(datetime.datetime.now() - self.final_json['initial_timestamp'])

        try:
            utils.db_data_writing(self.db_credential, db_name, self.final_json)
            print('file saved')

        except:
            # If db saving fails then save the final_json as json file
            print('failed db saving')
            with open(f"json_{self.final_json['timestamp']}", "w") as stream:
                json.dump(self.final_json, stream)

# =============================================================================
# =============================================================================
# Plot MetaClass
# =============================================================================
# =============================================================================
class PlotClass:
    """
    This metaclass is designed to collect all the routines to query and show results.
    In this metaclass are provided the basic functions to instantiate the connection with database and query on it.
    The contructor function will retrieve the db credential and the db name.
    THe db_name has to be manually feeded by the user, in order to connect with the correct data source.
    """
    @utils.db_configuration_retriever('.')
    def __init__(self, db_credential:dict, db_name:str):
        self.credential = db_credential
        self.db_name = db_name


    # =============================================================================
    # Query data
    # =============================================================================
    def query(self, selector_dict: dict, field_list: list):
        """
        Query

        This function is designet to automatically query on db data just providing a selector and a field list.



        Parameters
        ----------
        selector_dict : dict
                        dictionary containing db query following the cloudant standard
        field_list : list
                        list of field to retrieve for the queried elements
        Returns
        -------

        """
        return utils.db_data_query(self.credential, self.db_name, selector_dict, field_list)
