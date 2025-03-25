import math

user_input_ab : float = float(input("Enter the length of AB : "))
user_input_ac : float = float(input("Enter the length of AC : "))

def main(ab:float, ac:float):
    formula : float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {formula}")

if __name__ in "__main__":
    main(user_input_ab, user_input_ac)