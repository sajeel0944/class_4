def is_odd(value:int)->bool:
    remainder : int = value % 2
    return remainder == 1

def main():
    for i in range(11,1,-1):
        if is_odd(i):
            print(f"{i} odd", end=" ")
        else:
            print(f"{i} even", end=" ")

if __name__ in "__main__":
    main()