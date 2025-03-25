def add_arr(value:list[str]):
    print(f"Here's the list: {value}")

def main():
    arr : list[str] = []
    control_loop : bool = True
    while control_loop:
        user_input : str = input("Enter a value: ")
        if len(user_input) == 0 :
            break
        else:
            arr.append(user_input)
        
    return arr

if __name__ in "__main__":
    save = main()
    add_arr(save)
