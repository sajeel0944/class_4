def double_until_100(number:int) :
    while number < 100:
        number *= 2 
        print(number,end=" " )

def main():
    user_input = input("Enter a number: ")
    if user_input == "" :
        print("please enter number")
    else:
        convert_num : int = int(user_input)
        double_until_100(convert_num)

if __name__ in "__main__":
    main() 