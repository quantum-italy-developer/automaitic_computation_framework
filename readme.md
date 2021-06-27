# Computation Automatic Framework (CAF) 

This repository contains the implementation of a framework designed to run 
intensive calculation on remote powerfull server enablign to:

* **Parallelization**: Launching many calculation on the same time 
* **Automatic data gathering**: Collecting results coming from the
  calculation on the on line database.
* **Centralization**:  The database acts as a common data collector that can
be shared among team members and research community.


### Requirements

- Python 3.7
- cloudant 2.14

all the other requirements are contained into the `environment.yml`. 

**important**: 
We strongly advice to create a dedicated virtual python environment using 
[conda](https://docs.conda.io/projects/conda/en/latest/index.html) or 
one of the other solutions.

### Setup
1. Clone the repository on local machine where calculation will be executed.

1. Fill the `private_config.json` containing the following information:
    - Cloudant database credential
    - IBMQ credential
1. Implement the execution and plot classes following the example provided in the implementation folder and following
   the guidelines of the metaclasses in the CAF folder
1. Customize the `config.json` adapting data to the needs of the main module that
    will drive the simulation.

## How to contribute

Contributions are welcomed as long as the stick to the **git-flow**: fork 
this repo, create a local branch named 'feature-XXX'. Commit often. Split 
it in multiple commits and request a merge to the mainline often. 

To add new contribution please remember to follow 
[PEP 8](https://www.python.org/dev/peps/pep-0008/)
style guide, add enough comments to let the code unrstandable to other a
user/developer and add detailed docstring followingn the [numpy](https://numpydoc.readthedocs.io/en/latest/format.html)
style.

## Authors

This project has been developed thanks to the effort of the following people:

- Antonello Aita 
- Luca Crippa
- Michele Grossi


## Usage

 
 