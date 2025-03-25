def average(num_1 : int=0 , num_2 : int = 0)->float:
    sum : int = num_1 + num_2
    return sum / 2

def main():
    num_1 = average(0, 10)
    num_2 = average(8, 10)
    
    final = average(num_1, num_2)
    print("num_1", num_1)
    print("num_2", num_2)
    print("final", final)


if __name__ in  "__main__":
    main()