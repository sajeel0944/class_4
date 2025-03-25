try:
    frist_num : int = int(input("Enter your first number : "))
    second_num : int = int(input("Enter your second number : "))


    all_operator : list = ["+", "-", "X", "%", "÷"]
    count : int = 1
    for get_value in all_operator:
        print(f"{count} : {get_value}")
        count += 1

    user_select_operator : int = int(input("select one option : "))
    select_operator = all_operator[user_select_operator -1]


    def main(num1:int, num2:int, operator:str):
        print(f"\nyou select this option : ({operator})")

        if operator == "+":
            answer = num1 + num2
            print(f"sum answer : {answer}")
        elif operator == "-":
            answer = num1 - num2
            print(f"minus answer : {answer}")
        elif operator == "X":
            answer = num1 * num2
            print(f"multiply answer : {answer}")
        elif operator == "%":
            answer = num1 % num2
            print(f"modulus answer : {answer}")
        elif operator == "÷":
            answer = num1 / num2
            print("division answer : {answer}")
        else:
            print("\nsome thing was wrong")

    if __name__ == '__main__':
        main(frist_num,second_num,select_operator)

except  Exception as e:
    print("\nplease enter the number")