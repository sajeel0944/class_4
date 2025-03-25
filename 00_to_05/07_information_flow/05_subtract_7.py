def subtract_seven(num):
    return num - 7  

def main():
    user_input = int(input("Enter a number: "))  
    result = subtract_seven(user_input)   
    print(f"Result after subtracting 7: {result}")   

if __name__ == "__main__":
    main()
