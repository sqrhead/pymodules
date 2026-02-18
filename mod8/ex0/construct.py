import sys
import os
import site
# Authorized
# sys, os, site modules, print()

if __name__ == "__main__":

    # check if inside virtual env
    if 'VIRTUAL_ENV' in os.environ:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent python: {sys.executable}")
        venv_path = os.environ.get('VIRTUAL_ENV')
        print(f"Virtual Enviroment: {os.path.basename(venv_path)}")
        print(f"Enviroment path: {venv_path}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        try:
            print(f"\nPackage installation path: \n{site.getsitepackages()[0]}")
        except Exception:
            print("Error: site.getsitepackages() error")
    else:
        print("MATRIX STATUS: You're still plugged in")

        print(f"\nCurrent python : {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate # On Windows")
        print("\nThen run this program again")
