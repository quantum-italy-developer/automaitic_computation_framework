=========
Metaclass
=========

This part of the framework contains the backbone of the computation and plot part.
There have been implemented metaclass of referement for the plot and computation class implementation
tailored for your own case.

.. important::
    Both classes take as input, when instantiated, data coming from a `private_config.json`, if the config file is missing
    then you can feed this information manually

.. autoclass:: CAF.MetaClass.ComputationClass
   :members:
   :special-members: __init__
   :private-members: __init__

.. autoclass:: CAF.MetaClass.PlotClass
   :members:
   :special-members: __init__
   :private-members: __init__
