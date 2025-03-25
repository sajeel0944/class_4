arr = [1, 2, 3, 4, 5]  


def access():
    index_number : int = int(input("Enter index to access: "))
    print(f"\nResult : {arr[index_number]}")

def modify():
    index_number : int = int(input("Enter index to modify: "))
    update_value : str = input("Enter new value: ")
    arr[index_number] = update_value 
    print(f"Updated List: {arr}")

def slice_1():
    start_index : int = int(input("Enter start index: "))
    end_index : int = int(input("Enter end index: "))
    try:
        print(f"Sliced List: {arr[start_index : end_index]}") 
    except ValueError as e:
        print("list out of range")

def main():
    print("\nCurrent list:", arr)
    print("\nChoose an operation: access, modify, slice")

    user_input = input("\nEnter operation: ").lower()

    if user_input == "":
        print("Not Found Your Option")
    elif user_input == "access":
        access()
    elif user_input == "modify":
        modify()
    elif user_input == "slice":
        slice_1()
    else:
        print("Something Was Wrong")


if __name__ in "__main__":
    main()