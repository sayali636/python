# Define custom exception
class MyError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(message)

# Function raising custom exception
def oops():
    raise MyError("Custom MyError occurred!", data=101)

# Catcher function
def catcher():
    try:
        oops()
    except IndexError as e:
        print("Caught IndexError:", e)
    except MyError as e:
        print("Caught MyError:", e.message, "| Extra Data:", e.data)

catcher()
