# Program 1: Currency Notes Calculation

amount = int(input("Enter the amount to be withdrawn: "))

notes_10 = amount // 10
amount %= 10

notes_5 = amount // 5
amount %= 5

notes_1 = amount  # remaining amount will be in 1-rupee notes

print("10 Rs notes:", notes_10)
print("5 Rs notes :", notes_5)
print("1 Rs notes :", notes_1)




# Program 2: Income Tax Calculation

basic = float(input("Enter annual basic salary: "))

if basic < 250000:
    tax = 0
elif basic <= 500000:
    tax = (basic - 250000) * 0.10
else:
    tax = (250000 * 0) + (250000 * 0.10) + (basic - 500000) * 0.20

print("Income Tax:", tax)



# Program 3: Find Quadrant of a Point

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

if x == 0 and y == 0:
    print("Point is at the Origin.")
elif x == 0:
    print("Point lies on the Y-axis.")
elif y == 0:
    print("Point lies on the X-axis.")
elif x > 0 and y > 0:
    print("Point lies in Quadrant 1.")
elif x < 0 and y > 0:
    print("Point lies in Quadrant 2.")
elif x < 0 and y < 0:
    print("Point lies in Quadrant 3.")
else:
    print("Point lies in Quadrant 4.")



# Program 4: Profit or Loss

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit of", sp - cp)
elif sp < cp:
    print("Loss of", cp - sp)
else:
    print("No profit, no loss.")


    # Program 5: Sum of digits

num = int(input("Enter a number: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits of", num, "is", total)





# Program 6: Armstrong Number Check

num = int(input("Enter a number: "))
order = len(str(num))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit*digit*digit
    temp //= 10

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Program 7: Perfect Number Check

num = int(input("Enter a number: "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print(num, "is a Perfect number.")
else:
    print(num, "is not a Perfect number.")



# Program 8: Calculate X^Y

x = float(input("Enter value of X: "))
y = float(input("Enter value of Y: "))
result = x ** y
print(f"{x} raised to power {y} is {result}")


# Program 9: Palindrome Number Check

num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print(num, "is a Palindrome number.")
else:
    print(num, "is not a Palindrome number.")



# Program 10: Sum of first and last digit

num = int(input("Enter a number: "))
num_str = str(num)
first_digit = int(num_str[0])
last_digit = int(num_str[-1])
total = first_digit + last_digit

print("Sum of first and last digit of", num, "is", total)

# Program 11: Count even, odd, and zero digits

num = input("Enter a number: ")

even_count = odd_count = zero_count = 0

for digit in num:
    if digit == '0':
        zero_count += 1
    elif int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even digits:", even_count)
print("Odd digits :", odd_count)
print("Zero digits:", zero_count)

# Program 12:
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print("Decimal value:", decimal)


# Program 13: Check value between 1 and 50 from command line
import sys

if len(sys.argv) != 2:
    print("Usage: python program.py <number>")
else:
    try:
        value = int(sys.argv[1])
        if 1 <= value <= 50:
            print("Ok")
        else:
            print("Out of range")
    except ValueError:
        print("Please enter a valid integer.")



# Program 14: Prime numbers till N

n = int(input("Enter a number: "))

print("Prime numbers up to", n, "are:")
for num in range(2, n+1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


# Program 15: Multiplication tables for a range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end+1):
    print(f"\nMultiplication Table for {num}")
    for i in range(1, 11):
        print(num * i)




# Program 16:
#      1 
#    1 2 1 
#  1 2 3 2 1 
#1 2 3 4 3 2 1 



n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    # Print spaces for alignment
    print("  " * (n - i), end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # Move to next line



