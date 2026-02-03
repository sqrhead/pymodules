
# Require: file from the data given
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        with open("classified_data.txt", "r") as file:
            print("SECURE EXTRACTION:")
            data = file.read()
            print(data)
        with open("preservation_data.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived")
            print("\nSECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    except Exception:
        print("[ERROR] : DAWG CMON :>")
    finally:
        print("\nAll vault operations completed with maximum security.")
