def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    num = int(input("Enter your number: "))
    print(f"The factorial of {num} is {factorial(num)}")
