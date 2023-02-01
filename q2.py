def addition_function(x, y):
    answer = x + y
    return answer


def subtraction_function(x, y):
    answer = x - y
    return answer


def multiply_function(x, y):
    answer = x * y
    return answer


def division_function(x, y):
    answer = x/y
    return answer


def main():
    iterations = int(input("Hi, how many operations do you want MagiCal to perform?\n"))
    for i in range(iterations):
        operator_select = int(input("Select the operator from the list of Addition (1), Subtraction (2), "
                                    "Multiplication (3), Division (4):\n"))
        if operator_select in [1, 2, 3, 4]:
            x = int(input("Enter the first number in the interval of [0,100]:\n"))
            y = int(input("Enter the second number in the interval of [0,100]:\n"))
        else:
            print("Invalid input!")
            exit()

        if -1 < x < 101 and -1 < y < 101:
            if operator_select == 1:
                print(f"{x} + {y} = {addition_function(x, y)}")
            elif operator_select == 2:
                print(f"{x} - {y} = {subtraction_function(x, y)}")
            elif operator_select == 3:
                print(f"{x} * {y} = {multiply_function(x, y)}")
            elif operator_select == 4 and y != 0:
                print(f"{x} / {y} = {division_function(x, y)}")
                if y == 0:
                    print("The denominator cannot be 0.")

        else:
            print("Magic calculator can not perform your operation!")


if __name__ == '__main__':
    main()
