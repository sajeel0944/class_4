import random 

number_dice : int = 8

def dice_roll():
    dice1 : int = random.randint(1 ,number_dice)
    dice2 : int = random.randint(1 ,number_dice)
    total_dice = dice1 + dice2
    return total_dice

def main():
    dice : int = 12
    print(f"\ndie1 in main() starts as: {dice}\n")
    for get in range(2):
        total = dice_roll()
        print(f"Total of two dice: {total}")
    
    print(f"\ndie1 in main() is: {dice}" )


if __name__ in "__main__":
    main()