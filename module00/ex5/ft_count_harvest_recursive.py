def rec_fun(days: int, index: int):
    if index <= days:
        print(f"Day {index}")
        index = index + 1
        rec_fun(days, index)
    return


def ft_count_harvest_recursive():
    days: int = int(input("Days until harvest : "))
    rec_fun(days, 1)
    print("Harvest time!")
    return
