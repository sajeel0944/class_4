user_input_1 : int = int(input("Please enter an integer to be divided: "))
user_input_2 : int = int(input("Please enter an integer to divide by: "))

def main(dividend:int, divisor:int):
    quotient : int = dividend // divisor
    remainder : int = dividend % divisor
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ in "__main__":
    main(user_input_1, user_input_2)