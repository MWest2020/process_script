#!/usr/bin/env python3
import subprocess
import sys
import os
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
    
    # Command to execute using path variables
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"process_1944_pslist_{timestamp}.txt")
    
    # Build command as list of arguments
    cmd = ["python", vol_path, "-f", mem_path, "windows.pslist", "--pid", "1944"]
    
    print(f"\nExecuting: {' '.join(cmd)}")
    print(f"Output will be saved to: {output_file}")
    
    try:
        # Execute command and redirect only stdout to file, let stderr go to terminal
        with open(output_file, 'w') as f:
            result = subprocess.run(
                cmd,
                stdout=f,
                stderr=None,  # Let stderr go to terminal
                text=True,
                cwd=parent_dir,
                timeout=60
            )
                
    except subprocess.TimeoutExpired:
        print("Command timed out after 60 seconds!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
