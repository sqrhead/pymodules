import sys

if __name__ == "__main__":

    # check if inside virtual env
    if sys.prefix != sys.base_prefix:
        print("INSIDE VENV")
        print(f"{sys.prefix}")
    else:
        print("OUTSIDE VENV")
        print(f"{sys.prefix}")
