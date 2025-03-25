import random 

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for i in range(N_NUMBERS):
        ram = random.randint(MIN_VALUE,MAX_VALUE) 
        print(ram, end=" ") 

if __name__ in "__main__":
    main()


