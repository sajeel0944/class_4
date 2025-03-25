def manage(year:int):
    if year % 4 == 0:  
        if year % 100 == 0: 
            if year % 400 == 0:  
                print("That's a leap year!")
            else: 
                print("That's not a leap year.")
        else: 
            print("That's a leap year!")
    else: 
            print("That's not a leap year.")

def main():
    try:
        user_input : int = int(input("How old are you? "))
        manage(user_input)
    except ValueError:
        print("Enter Only Number")

if __name__ in "__main__":
    main()