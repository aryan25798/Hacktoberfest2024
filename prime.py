def is_prime(n):
    if n <= 1:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Divisible by a number other than 1 and itself
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
