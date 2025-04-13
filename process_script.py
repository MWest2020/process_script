#!/usr/bin/env python3
import subprocess
import sys
import os
import json
import glob
import shutil
from datetime import datetime

def main():
    # Define paths
    parent_dir = os.path.dirname(os.getcwd())
    vol_path = os.path.join(parent_dir, "volatility3", "vol.py")
    mem_path = os.path.join(parent_dir, "sample.mem")
    output_dir = os.path.join(os.getcwd(), "output")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load configuration from config.json
    config_path = os.path.join(os.getcwd(), "config.json")
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        pids = config.get('pids', [])
    except Exception as e:
        print(f"Error loading config file: {e}", file=sys.stderr)
        print("Using default PID: 1944")
        pids = [1944]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Run the exact commands from the README file for each PID
    for pid in pids:
        # Command 1: vol -f sample.mem windows.pslist --pid <PID>
        pslist_output = os.path.join(output_dir, f"process_{pid}_pslist_{timestamp}.txt")
        pslist_cmd = f"python {vol_path} -f {mem_path} windows.pslist --pid {pid} > {pslist_output}"
        print(f"\nExecuting: {pslist_cmd}")
        subprocess.run(pslist_cmd, shell=True, cwd=parent_dir)
        print(f"Command completed. Output saved to {pslist_output}")
        
        # Command 2: vol -f sample.mem windows.memmap --dump --pid <PID>
        memmap_output = os.path.join(output_dir, f"process_{pid}_memmap_{timestamp}.txt")
        memmap_cmd = f"python {vol_path} -f {mem_path} windows.memmap --dump --pid {pid} > {memmap_output}"
        print(f"\nExecuting: {memmap_cmd}")
        subprocess.run(memmap_cmd, shell=True, cwd=parent_dir)
        print(f"Command completed. Output saved to {memmap_output}")
        
        # Move dump file from parent directory to output directory
        source_dump = os.path.join(parent_dir, f"pid.{pid}.dmp")
        if os.path.exists(source_dump):
            dest_dump = os.path.join(output_dir, f"pid.{pid}.dmp")
            shutil.move(source_dump, dest_dump)
            print(f"Moved dump file from {source_dump} to {dest_dump}")
        else:
            print(f"Warning: No dump file found at {source_dump}")
        
        # Command 3: vol -f sample.mem windows.handles --pid <PID>
        handles_output = os.path.join(output_dir, f"process_{pid}_handles_{timestamp}.txt")
        handles_cmd = f"python {vol_path} -f {mem_path} windows.handles --pid {pid} > {handles_output}"
        print(f"\nExecuting: {handles_cmd}")
        subprocess.run(handles_cmd, shell=True, cwd=parent_dir)
        print(f"Command completed. Output saved to {handles_output}")
    
    # After all Volatility commands, run strings on the dump files
    for pid in pids:
        # Check if the dump file exists in the output directory
        dump_file = os.path.join(output_dir, f"pid.{pid}.dmp")
        if os.path.exists(dump_file):
            strings_output = os.path.join(output_dir, f"strings_{pid}_{timestamp}.txt")
            strings_cmd = f"strings -n 6 {dump_file} > {strings_output}"
            print(f"\nExecuting: {strings_cmd}")
            subprocess.run(strings_cmd, shell=True)
            print(f"Command completed. Output saved to {strings_output}")
        else:
            print(f"No memory dump file found for PID {pid} at {dump_file}. Skipping strings command.")

if __name__ == "__main__":
    main()
