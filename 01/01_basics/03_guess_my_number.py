import random

def find_number(num:int)->str:
    secret_number : int = random.randint(1, 99)

    if num == secret_number:
        return("Your guess is correct")
    elif num > secret_number:
        return("Your guess is too high")
    elif num < secret_number:
        return("Your guess is too low")
    else:
        return("invalid guess")


def main():
    print("I am thinking of a number between 1 and 99...\n")
    while True:
        user_guess = input("Enter a guess: ")
        if user_guess == "":
            print("Good BY")
            break
        else:
            print(find_number(int(user_guess)))


if __name__ in "__main__":
    main()





