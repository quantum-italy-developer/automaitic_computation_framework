"""
Utils
=========================
This module collect function used across the whole package


#todo: continue description

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
              'Michele Grossi <>'
              )
# Maintainer
__maintainer__ = ''
# Email of the maintainer
__email__ = ''

# =============================================================================
# Import modules
# =============================================================================
# Import general purpose module(s)
import cloudant
import pandas as pd
import itertools
import json
import os

# Import custom module(s)




# =============================================================================
# =============================================================================
# DATABASE FUNCTIONS
# =============================================================================
# =============================================================================

# =============================================================================
# DB data writing
# =============================================================================
def db_data_writing(credential:dict, db_name:str, files:dict):
    """
    DB data writing

    This function reach the online database and write the input files as a new document

    Parameters
    ----------
    credential: dict
                credential to access the online Cloudant database instance
    db_name: str
                name of the database on which write data
    files: dict
                json containing data to write on db
    Returns
    -------
    bool
        exit status

    """

    # Feed credential and establish a connection
    client = cloudant.Cloudant(credential["username"],credential["password"],url=credential["url"])
    client.connect()

    # Select the database instance on which write results
    db = client[db_name]

    # write and save document
    db.create_document(files).save()

    # shutdown the connection
    client.disconnect()

# =============================================================================
# DB data query
# =============================================================================
def db_data_query(credential:dict, db_name:str, selector_dict:dict, fields_list:list ):
    """
    DB data query

    This function query the db and retrieve data as list of json
    """
    # Connection to the db instance
    ## get data from credential json retrieved from the "service credential" created on the instance
    client = cloudant.Cloudant(credential["username"],credential["password"],url=credential["url"])
    client.connect()

    # from the instance select db
    db = client[db_name]

    documents = db.get_query_result(selector=selector_dict, fields=fields_list)

    return documents


# =============================================================================
# Input json organizer
# =============================================================================
def input_organizer(json_config_master:dict, mod = 'tuple')->dict:
    """
    Input json organizer

    This function take in input a json and then create a series of one-shot config file to feed a singular
    instance of simulation

    Parameters
    ----------
    json_config_master
    mod

    Returns
    -------

    """
    json_master = json_config_master['master']
    json_driver = json_config_master['variables']


    # Choose modality
    if mod == 'tuple':

        df_driver_raw = pd.DataFrame(json_driver)

        df_driver = df_driver_raw

        for value in df_driver.iterrows():

            for field in df_driver.columns:
                # Update values

                json_master[field] = value[1][field]

            key = ""

            for i, j in value[1].items():
                key += str(i) + '_' + str(j) + '_'

            yield json_master, key

    elif mod == 'cartesian':
        # Create the cartesian product among the given input values
        #index = pd.MultiIndex.from_product(df_driver_raw.T.values)
        #df_intermediate = pd.DataFrame(index=index).reset_index()
        #df_intermediate.columns = df_driver_raw.columns

        #df_driver = df_intermediate
        # @Anto @Mic new method [6-12-2020]

        # create all possible combinations
        combo = list(itertools.product(*(list(json_driver.values()))))
        i = 0
        for x in combo:
            key = ""
            # Create the updated json to return
            key = ""
            for name in json_driver.keys():
                for k in json_master.keys():
                    if name in json_master[k]:
                        json_master[k][name] = x[i]
                        key += str(name) + '_' + str(x[i]) + '_'
                i += 1
            i=0

            #return
            yield json_master,key
        #
    else:
        print(f'the selected modality: {mod} is undefined. Please select "tuple" or "cartesian"')




# =============================================================================
# Decorator to select user from config file or from input function
# =============================================================================
def configuration_retriever(path):
     """
     Configuration Retriever

     This function is designed to attempt in retrieving user credential for the database and the IBMQ system following
     two ways:

     1) Searching the 'private_config.json' at the provided path and extract credetial
     2) Using credetial provided as input call the function

     Parameters
     ----------
     path: str
            path where 'private_config.json' is located

     Returns
     -------

     """
     def decorator(func):
         def wrapper(*arguments):
             try:
                 with open(os.path.join(path,'private_config.json'),'r') as pconfig:
                     private_configuration = json.load(pconfig)

                 print('Credential get from configuration file')

                 return func(arguments[0],db_credential=private_configuration['Cloudant'],ibmq_credential=private_configuration['IBMQ'])

             except:
                 try:
                     print('Credential get from function arguments')
                     return func(arguments[0],arguments[1],arguments[2])
                 except:
                    print('No credential provided')
                    return True
         return wrapper
     return decorator
# =============================================================================
# Decorator to select user from config file or from input function
# =============================================================================
def db_configuration_retriever(path):
    """
    Configuration Retriever

    This function is designed to attempt in retrieving user credential for the database following
    two ways:

    1) Searching the 'private_config.json' at the provided path and extract credetial
    2) Using credetial provided as input call the function

    Parameters
    ----------
    path: str
           path where 'private_config.json' is located

    Returns
    -------

    """
    def decorator(func):
        def wrapper(*arguments):
            try:
                with open(os.path.join(path,'private_config.json'),'r') as pconfig:
                    private_configuration = json.load(pconfig)

                print('Credential get from configuration file')

                return func(arguments[0],db_credential=private_configuration['Cloudant'],db_name=arguments[2])

            except:
                try:
                    print('Credential get from function arguments')
                    return func(arguments[0],arguments[1])
                except:
                    print('No credential provided')
                    return True
        return wrapper
    return decorator