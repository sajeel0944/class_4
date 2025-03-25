arr_length : int = 3

def shorten(value:list[str]):
    if len(value) > 3:
        while len(value) > 3:
            value.pop()
            print(value)
    else:
        print(value)

def main():
    arr : list[str] = []
    control_loop : bool = True
    while control_loop:
        user_input : str = input("Please enter an element of the list or press enter to stop : ")
        if len(user_input) == 0  :
            break
        else:
            arr.append(user_input)
    return arr

if __name__ in "__main__":
    save = main()
    shorten(save)
