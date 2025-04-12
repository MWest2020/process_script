Basically make a python that that runs:

vol -f sample.mem windows.pslist --pid 1944
vol -f sample.mem windows.memmap
strings [path to dump file]

vol -f sample.mem windows.handles --pid 1944

which gets the pid out a config.json
# process_script
