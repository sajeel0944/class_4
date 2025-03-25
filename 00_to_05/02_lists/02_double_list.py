def multiple(num:list[int]):
    total : list[int] = [] 
    for index in range(len(num)):
        index_value : int = num[index ]
        mul : int =  index_value * 2
        total.append(mul)

    return total

def main():
    arr : list[int] = [1,2,3,4,5,6]
    push_arr = multiple(arr)
    print(push_arr)

if __name__ in "__main__":
    main()