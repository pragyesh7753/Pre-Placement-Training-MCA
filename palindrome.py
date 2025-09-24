def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
