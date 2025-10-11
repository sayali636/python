# tools.py
import sys
import traceback

def safe(func, *args):
    try:
        return func(*args)   # call the function with arguments
    except Exception:
        exc_type, exc_value = sys.exc_info()[:2]
        print("Exception type:", exc_type)
        print("Exception value:", exc_value)
        print("Stack trace:")
        traceback.print_exc()
