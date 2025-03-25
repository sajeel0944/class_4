def manage_height(height: float):
    MIN_HEIGHT = 50  

    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    while True: 
        try:
            user_input : float = float(input("How tall are you? "))
            if user_input == "":
                break
        
            manage_height(user_input)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
