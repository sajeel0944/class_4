import random

number_of_side : int = 12

def main(number):
    die1 : int = random.randint(1 , number)
    die2 : int = random.randint(1 , number)

    total : int = die1 + die2

     # Print out the results
    print("\nDice have", number, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ in "__main__":
    main(number_of_side)