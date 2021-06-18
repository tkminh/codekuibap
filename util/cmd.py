import os
import subprocess

def run_command(cmd):
    os.system(cmd)
    print("Done !")

def execute_cmd(cmd, params = ''):
    subprocess.run([cmd, params], stdout=subprocess.PIPE, text=True)
    print("Done !")