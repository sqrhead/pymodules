# Require: file from the data given
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", mode="r")
        content = file.read()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
