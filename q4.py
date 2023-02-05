def valid_check(user_input):
    if 2 < user_input < 9:
        return True

    else:
        print("PyNum cannot help you!")
        return False

def PyNum(h):
    for rows in range(h):
        for columns in range(h):
            print(columns, end=" ")
        print("\n")


def main():
    h = int(input("What is the height of the pyramid?\n"))
    if valid_check(h):
        PyNum(h)



if __name__ == '__main__':
    main()
