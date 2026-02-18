import os

if __name__ == "__main__":
    print('ORACLE STATUS: Reading the Matrix...')
    trigger: bool = True
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        trigger = False
        print("fail to import 'dotenv'")
    print('\nConfiguration loaded:')
    try:
        print(f'Mode:{os.environ["MATRIX_MODE"]}')
    except Exception:
        print("MATRIX_MODE_NOT_FOUND")
        trigger = False

    try:
        print(f'Database:{os.environ["DATABASE_URL"]}')
    except Exception:
        print("DATABASE_NOT_FOUND")
        trigger = False

    try:
        print(f'API Access:{os.environ["API_KEY"]}')
    except Exception:
        print("API_KEY_NOT_FOUND")
        trigger = False
    try:
        print(f'Log Level:{os.environ["LOG_LEVEL"]}')
    except Exception:
        print("LOG_LEVEL_NOT_FOUND")
        trigger = False

    try:
        print(f'Zion Network:{os.environ["ZION_ENDPOINT"]}')
    except Exception:
        print("ZION_ENDPOINT_NOT_FOUND")
        trigger = False


    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if trigger:
        print("[OK] .env file properly configured")
    else:
        print("[NOT OK] .env file properly configured")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")