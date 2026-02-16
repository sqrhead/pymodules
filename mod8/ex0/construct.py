import sys

# Authorized
# sys, os, site modules, print()

if __name__ == "__main__":

    # check if inside virtual env
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        # Current Python: /usr/bin/python3.11 -> current python interpreter used
        # Virtual Environment: None detected -> folder where venv is
        # /path/to/matrix_env/lib/python3.11/site-packages -> where packages are installed
        print("INSIDE VENV")
        print(f"{sys.prefix}")
    else:
        print("OUTSIDE VENV")
        print(f"{sys.prefix}")
