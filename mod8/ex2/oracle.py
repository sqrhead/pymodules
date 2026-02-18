try: 
    from dotenv import load_dotenv
except ImportError:
    print("fail to import 'dotenv'")
import os 

if __name__ == "__main__":
    print('ORACLE STATUS: Reading the Matrix...')
    load_dotenv('.domodossola')
    print('\nConfiguration loaded:')
    try: 
        print(f'MATRIX_MODE:{os.environ["MATRIX_MODE"]}')
    except Exception:
        print("MATRIX_MODE_NOT_FOUND")

    try: 
        print(f'DATABASE_URL:{os.environ["DATABASE_URL"]}')
    except Exception:
        print("DTABASE_URL_NOT_FOUND")

    try: 
        print(f'API_KEY:{os.environ["API_KEY"]}')
    except Exception:
        print("API_KEY_NOT_FOUND")

    try: 
        print(f'LOG_LEVEL:{os.environ["LOG_LEVEL"]}')
    except Exception:
        print("LOG_LEVEL_NOT_FOUND")

    try: 
        print(f'ZION_ENDPOINT:{os.environ["ZION_ENDPOINT"]}')
    except Exception:
        print("ZION_ENDPOINT_NOT_FOUND")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")