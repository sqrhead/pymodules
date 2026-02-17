import sys
import os 
# Authorized
# sys, os, site modules, print()

if __name__ == "__main__":

    # check if inside virtual env
    if 'VIRTUAL_ENV' in os.environ: # List of enviroment variables 
        # print("MATRIX STATUS: You're still plugged in")
        # Current Python: /usr/bin/python3.11 -> current python interpreter used
        # Virtual Environment: None detected -> folder where venv is
        # /path/to/matrix_env/lib/python3.11/site-packages -> where packages are installed
        print("=== INSIDE VENV ===")
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent python: {sys.executable}")
        print(f"Virtual Enviroment: {os.name}")
        print(f"Enviroment path: {os.environ['VIRTUAL_ENV']}")
        
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print(f"\nPackage installation path: \n{...}")
        # print(f"{sys.executable}") # python interpreter location 
        # print(f"{os.environ['VIRTUAL_ENV']}") # venv location
    else:
        print("=== OUTSIDE VENV ===")
        print("MATRIX STATUS: You're still plugged in")

        print(f"\nCurrent python : {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_venv\nScripts\nactivate # On Windows")
        print("\nThen run this program again")
        # print(f"{os.environ['VIRTUAL_ENV']}")

