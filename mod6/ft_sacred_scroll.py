import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")

    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire(): ", end='')
        print(f"{alchemy.elements.create_fire()}")
    except Exception as e:
        print("[ERROR] - Import Error")
    try:
        print("alchemy.elements.create_water(): ", end='')
        print(f"{alchemy.elements.create_water()}")
    except Exception as e:
        print("[ERROR] - Import Error")
    try:
        print("alchemy.elements.create_earth(): ", end='')
        print(f"{alchemy.elements.create_earth()}")
    except Exception as e:
        print("[ERROR] - Import Error")
    try:
        print("alchemy.elements.create_air(): ", end='')
        print(f"{alchemy.elements.create_air()}")
    except Exception as e:
        print("[ERROR] - Import Error")

    print()

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", end='')
        print(f"{alchemy.create_fire()}")
    except Exception as e:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_water(): ", end='')
        print(f"{alchemy.create_water()}")
    except Exception as e:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_earth(): ", end='')
        print(f"{alchemy.create_earth()}")
    except Exception as e:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_air(): ", end='')
        print(f"{alchemy.create_air()}")
    except Exception as e:
        print("AttributeError - not exposed")

    print("\nPackage metadata: ")
    print(f"Version: {alchemy.__version__}")
    print(f"Author : {alchemy.__author__}")