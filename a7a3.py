# Define custom exception with extra data
class MyError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(message)

# Function raising MyError
def oops():
    raise MyError("This is a custom MyError!", data=404)

# Catcher function handling both exceptions
def catcher():
    try:
        oops()
    except IndexError as e:
        print("Caught an IndexError:", e)
    except MyError as e:
        print("Caught MyError:", e.message, "| Extra Data:", e.data)

catcher()
