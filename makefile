# makefile designed to easly launch the comprensive main function
# to run the comprensive_main script type: make run
run:
	nohup python comprehensive_main.py -in config_repo/config_master.json -e config_repo -ef single_main.py > run.log &
