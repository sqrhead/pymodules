def ft_count_harvest_iterative():
    days: int = int(input("Days until harvest : "))
    index: int = 1
    while index <= days:
        print(f"Day {index}")
        index = index + 1
    print("Harvest time!")
