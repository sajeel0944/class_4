AGE : int = 18 

def adult(age: int) -> bool:
    if age >= AGE:
        return True
    
    return False
    

def main():
    age : int = int(input("How old is this person?: "))
    print(adult(age))
    

if __name__ == "__main__":
    main()