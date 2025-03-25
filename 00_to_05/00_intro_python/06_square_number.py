try:
    user_input : int = int(input("Enter a number to see its square : "))

    def main(square_value:int):
        convert_square : int = square_value ** 2
        print(f"\n{square_value} squared is {convert_square}")

    if __name__ in "__main__":
        main(user_input)

except ValueError:
    print("\nPlease enter only number")