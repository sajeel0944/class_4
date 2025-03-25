try:
    def first_element(value:int):
        print(f"Your First Element is '{value[0]}'")
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
        first_element(save)
except Exception as e:
    print("Enter your first element")