"""
Execution
=========================
This module contains some examples on how to implement a running class to perform calculation as quantum simulation or
run on a real device.
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
              'Michele Grossi <michele.grossi@cern.ch>')
# Maintainer
__maintainer__ = ''
# Email of the maintainer
__email__ = ''

# =============================================================================
# Import modules
# =============================================================================
# Import general purpose module(s)

# Import custom module(s)
from CAF.MetaClass import ComputationClass


# =============================================================================
# Create logger
# =============================================================================
# todo valutare se tenere


# =============================================================================
# CALCULATION CLASS
# =============================================================================
class Calculation(ComputationClass):
    """
    This class
    """

    def __init__(self,
                 var_1: str,
                 var_2: int):
        """"""
        # Referement to the superclass
        super().__init__()

        # Report the input parameters into the final_json, legacy from the meclass, in order to be ready to be saved
        # as metadata for the executed run
        self.final_json["var_1"] = var_1
        self.final_json["var_2"] = var_2

    # =============================================================================
    # Internal function
    # =============================================================================
    def _internal_func(self):
        """
        Internal Function

        This is a special kind of function designed to be executed as internal class methods (private class method).
        They are designed to split activities in smaller and smarter functions.

        Returns
        -------
        """
        pass
    # =============================================================================
    # Run Function
    # =============================================================================
    def run(self):
        """
        Run Function

        This function has to be declared in order to replace the one coming from the metaclass.
        This is a foundamental function because it is called in the main script in order to perform calculation.
        Obviously it is possible to design many other public methods, depending on the computational task of the class.

        Returns
        -------

        """
        pass