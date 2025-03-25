def make_arr(value:str):
    arr_data:list[str] = []
    print(f"List before: {arr_data} ")
    for x in range(3):
        arr_data.append(value)

    return arr_data

def main():
    user_input : str = input("Enter a message to copy: ")
    push_data = make_arr(user_input)
    print(f"List after: {push_data}")

if __name__ in "__main__":
    main()