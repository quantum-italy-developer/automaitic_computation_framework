"""
Plot
=========================
This modules collects all the functions dedicated to plot data retrieved from the database.

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
__author__ = ('Antonello Aita <antonello.aita@gmail.com>',
              'Luca Crippa <>',
              'Michele Grossi <michele.grossi@cern.ch>'
              )
# Maintainer
__maintainer__ = ''
# Email of the maintainer
__email__ = ''

# =============================================================================
# Import modules
# =============================================================================
# Import general purpose module(s)
# Import custom module(s)
from CAF.MetaClass import PlotClass
# todo: da rivedere la struttura della classe perchè ci sarebbe da separare le componenti di post processing da
#  quelle di plot ed inoltre rendere più fluida la classe evitando di far uscire ed entrare gli argomenti dele funzioni
#  hint: meglio salvarle nel self oppure usare funzioni nascoste
# =============================================================================
# =============================================================================
# Plot class
# =============================================================================
# =============================================================================
class Plot(PlotClass):
    """
    This class is built on top of the PortClass structure. From this one it ineriths the methods:
        1) __init__(db_name)
        2) query()

    This class will automatically connect to the db using the credential provided in the private_config.json,
    the inerith init method needs to be feed with the db name, so when you will instantiate the class you have
    to provide the db_name, of a db already existing in your account.

    each function of the class has to be designed following this structure:
    1) selector contruction
    2) field list construction
    3) data retrieving using query()
    4) data post-processing (*)
    5) plot design

    (*): if the post-process function increase too much, in order to design a readable code it is possible to collect
    the post-process function into a pre-defined script

    """
    # =============================================================================
    # Main DB data extraction and post-processing
    # =============================================================================
    def plot_example(self, var_1:str, var_2:int):
        """

        Returns
        -------

        """
        # 1) Selector contruction
        selector = {
                    "var_1": var_1,
                   }

        # 2) Fild list contruction
        field_list = [var_2]

        # 3) db data retrieving
        db_data = self.query(selector, field_list)

        # 4) data post - processing

        # 5) plot design


