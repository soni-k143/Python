# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

num = int(input("Enter a number: "))

def cal(num):
    squ = math.sqrt(num)
    log = math.log(num)
    sin = math.sin(num)

    print(f"Square root: {squ}")
    print(f"Logarithm: {log}")
    print(f"Sine: {sin}")

cal(num)
