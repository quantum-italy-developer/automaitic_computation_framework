import json
from implementation.execution import Calculation
import argparse
'''

Function to run calculation upon the built class (Calculation)

'''
parser = argparse.ArgumentParser()
parser.add_argument('-in', '--input', type=str, required=True)
args = parser.parse_args()
print(args.input)
# =============================================================================
# Private config file reading
# =============================================================================
try:
    with open('private_config.json') as pconfig:
        private_configuration = json.load(pconfig)
except:
    print("Error in reading private config: Process aborted")
# =============================================================================
# config file reading
# =============================================================================
try:
    with open(args.input) as run_config:
        run_configuration = json.load(run_config)
        print(' Reading config file...')
except Exception as exc:
    print("Error in reading temp config: Process aborted")
    print(f" Error retriven: ({exc})")

if __name__ == "__main__":

    print("\n ********** single main *********")
    print(run_configuration)

    ## Simulation Workflow

    a = Calculation(**run_configuration['master']['init'])

    a.run(**run_configuration['master']['run'])

    a.save(**run_configuration['db_name']['save'])

    print('run completed!')
