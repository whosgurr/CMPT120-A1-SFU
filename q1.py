def chat_start():
    response = input("Hi, this is Pchatbot, can I talk to you?\n")
    if response in ["Y", "y"]:
        return True
    if response in ["N", "n"]:
        print("Okay! Talk to you soon!")
        return False


def name_inquiry():
    name = input("What is your name?\n")
    print(f"Nice to meet you, {name}.")
    return name


def mood_inquiry():
    name = name_inquiry()
    mood = input("How are you doing today?\n")
    if mood in ["Good", "I'm great", "I'm good", "Fine"]:
        print(f"I'm glad you're feeling well, {name}.")
        return True
    elif mood in ["Bad", "Not Okay", "I'm not feeling good"]:
        print("Have some time to yourself to recharge!")
        return False
    else:
        print("I see!")
        return False


def age_inquiry():
    try:
        age = int(input("How old are you?\n"))
        if age > 18:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    if chat_start():
        mood = mood_inquiry()
        age = age_inquiry()
        if mood and age:
            print("You are ready to drive.")
        else:
            print("Still taking the bus!")


if __name__ == "__main__":
    main()
