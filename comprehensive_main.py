import json
import argparse
import subprocess, os, sys
import time

from CAF.utils import input_organizer

'''

Function to run VQE for the Heisenberg use case. Read from config file.

USAGE (1): python comprehensive_main.py -in folder_containing_configfile/config_master.json
           given a config master the main creates a set of temporary configfile and run many parallel processes [currently it doesn't woerk]
or

USAGE (2): python comprehensive_main.py -in folder_containing_configfile/config.json -e folder_containing_configfile
           given a config master the main creates a set of temporary configfile, save them on the config folder, and then run the single_main script against eeach config folder

'''
parser = argparse.ArgumentParser()
parser.add_argument('-in', '--input', type=str, required=True)
parser.add_argument('-ef', '--execution_file', type=str, required=True)
parser.add_argument('-e', '--external', type=str, required=False)  # add the path of config file
args = parser.parse_args()
print(args.input)
# =============================================================================
# config file reading
# =============================================================================
try:
    with open(args.input) as run_config:
        run_configuration = json.load(run_config)
        print(' Reading config file...')
except:
    print("Error in reading master config: Process aborted")

if __name__ == "__main__":
    ## Simulation Workflow
    if args.external:
        # json_path = os.path.join(args.external,'temporary.json')
        json_list = []
        procs = []
        iterator = 0
        for json_config, key in input_organizer(run_configuration, mod='cartesian'):
            iterator += 1
            json_path = os.path.join(args.external, f'temporary_{iterator}.json')
            json_list.append(json_path)
            open(json_path, 'w').write(json.dumps(json_config))
            print(json_config)
            time.sleep(2)
            # subprocess.Popen([sys.executable,"single_main.py","-in",json_path])
            proc = subprocess.Popen([sys.executable, args.execution_file, '-in', json_path])
            procs.append(proc)
            print(proc.pid)

        for proc in procs:
            proc.wait()

        for js_path in json_list:
            os.remove(js_path)
    else:
        print('Error occurred! no external config provided')
