def main():
    user_input = input("Enter a number: ")
    if user_input :
        convert_num : int = int(user_input)
        while convert_num < 100:
            convert_num *= 2
            print(convert_num , end=" ")

if __name__ in "__main__":
    main()