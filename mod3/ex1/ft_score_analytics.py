import sys

#sys.argv, len(), sum(), max(), min(), int(), print()
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv_len: int = len(sys.argv)
    index: int = 1
    lst: list[int] = []

    if argv_len < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..")
    else:
        while index < argv_len:
            try:
                lst = lst + [int(sys.argv[index])]
                if int(sys.argv[index]) < 0:
                    raise Exception("Error: Negative number not valid")
            except ValueError:
                print(f"Error: {sys.argv[index]} is not valid!")
                raise SystemExit # is valid to use ?
            except Exception as e:
                print(f"{e}")
                raise SystemExit
            index += 1
        print(f"Scores processed: {lst}")
        print(f"Total players: {len(lst)}")
        print(f"Total scores: {sum(lst)}")
        print("Average score: %.1f" % (sum(lst) / len(lst)))
        print(f"High score: {max(lst)}")
        print(f"Low score: {min(lst)}")
        print(f"Score range: {max(lst) - min(lst)}")

