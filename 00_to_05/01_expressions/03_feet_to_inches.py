print("\n\t\t\tWellcome To Feet Convert Into Inches\n")

user_input : int = int(input("Enter number of feet : "))

def main(feet:int):
    inche : int = 12
    convert : int = feet * inche
    print(f"That is {convert} inches")

if __name__ in "__main__":
    main(user_input)