def is_not_multiple(number):
    for i in range(2, number):
        if number % i == 0:
            return True
    return False


def user_prompt():

    num_primes = 0
    iterations = int(input("How many numbers do you want to check?\n"))

    for i in range(iterations):
        n = int(input("Enter a positive integer:\n"))
        if n % 2 == 0 and n != 2:
            continue

        elif n < 0:
            print("PrimeFinder ignores negative numbers!")
            iterations += 1

        else:
            print(f"{n} is a prime number.")
            num_primes += 1

    print(f"Total prime numbers: {num_primes}")


def main():
    user_prompt()


if __name__ == '__main__':
    main()
