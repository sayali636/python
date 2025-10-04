# Write a python script to generate Fibonacci terms using generator function.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example
for num in fibonacci(10):
    print(num, end=" ")
