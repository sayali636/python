# User-defined exception
class InvalidDateException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Date: {self.day:02d}/{self.month:02d}/{self.year}")

    @staticmethod
    def validate(day, month, year):
        # Check month
        if month < 1 or month > 12:
            raise InvalidDateException("Invalid Month! Must be between 1 and 12.")
        # Days in each month
        days_in_month = [31, 29 if Date.is_leap(year) else 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]
        if day < 1 or day > days_in_month[month - 1]:
            raise InvalidDateException("Invalid Day for the given month/year.")
        if year < 1:
            raise InvalidDateException("Invalid Year! Must be positive.")

    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# ---- MAIN PROGRAM ----
try:
    d = int(input("Enter day: "))
    m = int(input("Enter month: "))
    y = int(input("Enter year: "))

    Date.validate(d, m, y)
    mydate = Date(d, m, y)
    mydate.display()

except InvalidDateException as e:
    print("Date Error:", e)
