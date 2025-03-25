data = []

def save_value(num:int):
    push_value = data.append(num)
   

def count_nums():
    
    print("\nNumber Count:\n")
    count_dict = {} 

    for num in data:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        print(f"{num} appears {count} times.")


def main():
    while True:
        user_input = input("Enter your number ")
        if user_input.isdigit() :
            convert_num : int = int(user_input)
            save_value(convert_num)
        elif user_input == "":
            count_nums()
            break
        else:
            print("\nEnter Only Number\n")


if __name__ in "__main__":
    main()




