def fibonacci(n, fib={}):
    if n in fib:
        return fib[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1, fib) + fibonacci(n - 2, fib)
    fib[n] = result
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Fibonacci of {n} is {fibonacci(n)}")
