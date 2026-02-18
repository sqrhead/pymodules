# create venv and install libraries with pip/poetry

if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    data = None
    panda_data = None
    try:
        import requests as req
        print(f"[OK] requests ({req.__version__}) - Network access ready")

    except Exception:
        print("[NOT OK] requests missing - [None]")
    try:
        # numpy is a math library
        import numpy as np
        data = np.random.rand(1000, 2)
    except Exception:
        print("[NOT OK] numpy missing - [None]")

    try:
        # pandas is a manipulation data library
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__})- Data manipulation ready")
        panda_data = pd.DataFrame(data)
    except Exception:
        print("[NOT OK] panda missing - [None]")
    try:
        # matplotlib let you do cool stuff with data
        # like visualization in different way
        import matplotlib as mat
        from matplotlib import pyplot as plt
        print(f"[OK] matplotlib ({mat.__version__}) - Visualization ready")
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...")
        panda_data.plot()
        plt.savefig('matrix_analysis.png')
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png}")
    except Exception:
        print("[NOT OK] matplotlib missing - [None]")
