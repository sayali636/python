# Function that raises IndexError
def oops():
    raise IndexError("This is an IndexError raised intentionally!")

# Catcher function
def catcher():
    try:
        oops()
    except IndexError as e:
        print("Caught an IndexError:", e)

catcher()
