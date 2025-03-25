def sum(num1:int, num2:int):

    sum_number : int = num1 + num2
    print(f"Answer : {sum_number}")

def main():
    frist_num : int = input("Enter your first number : ")
    second_num : int = input("Enter your second number : ")


    if frist_num == "" and second_num == "":
        print("Please Enter Number")
    else:
        try:
            sum(int(frist_num), int(second_num))
        except ValueError as e:
            print("Enter Only Number")

if __name__ in "__main__":
    main()