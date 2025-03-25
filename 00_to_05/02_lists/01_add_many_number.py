def sum(number:list[int]):
    total = 0
    for get in number:
        total += get
    
    return total

def main():
    arr : list[int] = [1,2,3,4,5,6]
    push_arr = sum(arr)
    print(push_arr)

if __name__ in "__main__":
    main()