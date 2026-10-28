#!/usr/bin/python3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 * num2
if result > 0:
    sign = "positive"
elif result < 0:
    sign = "negative"
else:
    sign = "zero"
print(sign)
print(f"Result: {result}")