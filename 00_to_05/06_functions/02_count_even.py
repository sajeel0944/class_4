def count_even(num_list:list[int])->int:
    count = 0 
    for num in num_list:
        if num % 2 == 0 :
            count += 1
        
    return count

def num_list()->int:
    arr : list[int] = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            return(count_even(arr))
            break
        else:
            arr.append(int(user_input))

def main():
    print(num_list())

if __name__ in "__main__":
    main()
