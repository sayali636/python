# Program to read test.txt and handle values
try:
    with open("test.txt", "r") as f:
        for line in f:
            data = line.strip()
            try:
                # Try integer
                val = int(data)
                print(f"Integer found: {val}")
            except ValueError:
                try:
                    # Try float
                    val = float(data)
                    print(f"Float found: {val}")
                except ValueError:
                    # If not int/float, must be string/char
                    print(f"Character/String found: {data}")
except FileNotFoundError:
    print("Error: test.txt file not found!")
