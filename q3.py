
def is_not_multiple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def user_prompt():
    i = 0
    num_primes = 0

    iterations = int(input("How many numbers do you want to check?\n"))

    while i != iterations:
        n = int(input("Enter a positive integer:\n"))

        if n < 0:
            print("PrimeFinder ignores negative numbers!")
            i -= 1

        elif (n % 2 == 0 and n != 2) or n == 1:
            i += 1
            continue

        elif is_not_multiple(n):
            print(f"{n} is a prime number.")
            num_primes += 1
        i += 1

    print(f"Total prime numbers: {num_primes}")


def main():
    user_prompt()


if __name__ == '__main__':
    main()
