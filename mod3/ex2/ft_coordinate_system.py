import sys
import math
#sys, sys.argv, math, math.sqrt(), tuple(), int(), float(), split(), print()
#since sys is imported do i need to use the command line to give inputs?


def get_distance(tpl1: tuple, tpl2: tuple) -> float:
    (x1, y1, z1) = tpl1
    (x2, y2, z2) = tpl2
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def create_3d_coords(lst: list) -> tuple:
    x: int = int(lst[0])
    y: int = int(lst[1])
    z: int = int(lst[2])
    return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    deftpl: tuple = (0, 0, 0)
    tpl: tuple = (10, 20, 5)
    print(f"\nPosition created: {tpl}")
    print(f"Distance between {deftpl} and {tpl}:", end=" ")
    print("%.2f" % get_distance(deftpl, tpl))

    print('\nParsing coordinates: "3,4,0"')
    coords: str = "3,4,0"
    splitted: list = coords.split(sep=",")
    tpl_parse: tuple
    try:
        tpl_parse = create_3d_coords(splitted)
    except ValueError as ve:
        print(f"{ve}")
    print(f"Parsed position: {tpl_parse}")
    print(f"Distance between {deftpl} and {tpl_parse}:", end=" ")
    print("%.1f" % get_distance(deftpl, tpl_parse))

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    inv_coords: str = "abc,def,ghi"
    splitted: list = inv_coords.split(sep=",")
    tpl_parse: tuple
    try:
        tpl_parse = create_3d_coords(splitted)
    except ValueError as ve:
        print(f"Error parsing coordinate: {ve}")
        print(f'Error details - Type: ValueError, Args: ({ve})')

    print("\nUnpacking demonstration:")
    pack_tpl: tuple = (3, 4, 0)
    (x, y, z) = pack_tpl
    print(f"Player at x={pack_tpl[0]}, y={pack_tpl[1]}, z={pack_tpl[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

