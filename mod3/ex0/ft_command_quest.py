import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    av_len: int = len(sys.argv)
    index: int = 1
    lst: list[str] = []

    if av_len - 1 == 0:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if av_len - 1 > 0:
        print(f"Arguments received: {av_len - 1}")
        while index < av_len:
            print(f"Argument {index}: {sys.argv[index]}")
            index += 1
    print(f"Total arguments: {av_len}")