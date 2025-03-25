phone_data = []

def phone_number(name:str, num:int):
    phone_data.append({name : num})


def lookup(name_1:str):
    count : int = 0
    for i in phone_data:
        find_phone = phone_data[count].get(name_1,"")
        if find_phone:
            print(f"\nPhone {find_phone}")
        count += 1

   
def display():
    print("\nAll Phone Data\n")
    count : int = 0
    for entry in phone_data:  
        for name, num in entry.items():
            print(f"{name} -> {num}")

    user_name_2 : str = input("Enter name to lookup: ")
    lookup(user_name_2)


def main():
    while True:
        user_name : str = input("Name: ") 
        user_num = input("Number: ")

        if user_name and user_num :
            convert_number : int = int(user_num)
            phone_number(user_name, convert_number)
        elif not user_name :
            display()
            break



if __name__ in "__main__":
    main()

