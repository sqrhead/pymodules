
if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    try:
        import requests as req
        print(f"[OK] requests ({req.__version__}) - Network access ready")

    except Exception:
        print("[NOT OK] requests missing - [None]")
    try:
        import numpy as np
        data = np.random.rand(10, 2)
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__})- Data manipulation ready")
        panda_data = pd.DataFrame(data)
    except Exception:
        print("[NOT OK] panda missing - [None]")
    try:
        import matplotlib as mat
        from matplotlib import pyplot as plt
        print(f"[OK] matplotlib ({mat.__version__}) - Visualization ready")
        panda_data.plot()
        plt.savefig('matrix_analysis.png')
    except Exception:
        print("[NOT OK] matplotlib missing - [None]")
