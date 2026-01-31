
# Require: file from the data given
if __name__ == "__main__":

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt","r") as file:
            data = file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("/classified_vault.txt", "w") as file:
            file.write("damn")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    try:
        print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - ''{data}''")
    except Exception as e:
        print(f"[ERROR] : {e}")
        pass
    finally:
        print("STATUS: Normal operations resumed")
        pass

    print("\nAll crisis scenarios handled successfully. Archives secure.")


