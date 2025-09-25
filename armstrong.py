def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num


def armstrong_between_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
armstrong_numbers = armstrong_between_range(start, end)
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")
