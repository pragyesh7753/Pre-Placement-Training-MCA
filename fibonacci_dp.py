def fibonacci(n, fib={}):
    if n in fib:
        return fib[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1, fib) + fibonacci(n - 2, fib)
    fib[n] = result
    return result


def fibonacci_series(n):
    series = []
    for i in range(n + 1):
        series.append(fibonacci(i))
    return series


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    series = fibonacci_series(n)
    print(f"Fibonacci series up to {n}: {series}")
    print(f"Fibonacci of {n} is {fibonacci(n)}")
 