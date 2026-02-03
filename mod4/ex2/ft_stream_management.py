import sys
# sys.stdin.readline() not in the authorized
# sys.stdout.write() not in the authorized
# sys.stderr.write() not in the authorized
# i think i have to use them probably
# but then why is input() in the authorized?
# TODO: Find way to use sys.stdin and rest
# DAAAAAAAAAAAAAMN FUCK
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    try:
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        sysre1 = sys.stdin.readline().strip()
        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush()
        sysre2 = sys.stdin.readline().strip()
        sys.stdout.write(
            "[STANDARD] Archive status " +
            f"from {sysre1}: {sysre2}\n"
            )
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n"
            )
        sys.stdout.write("[STANDARD] Data transmission complete\n")

        print("Three-channel communication test successful.")
    except Exception as e:
        print("[ERROR] : DAMN DAWG AN ERROR OCCURED")
        print(f"[ERROR] : {e}")

