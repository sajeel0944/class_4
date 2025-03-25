def print_multiple(message:str, repeats:int):
     print("\n")
     for i in range(repeats):
         print(f"{message}" , end=" ")

def main():
    message = input("\nPlease type a message: ") 
    repeats = int(input("Enter a number of times to repeat your message: ")) 
    print_multiple(message, repeats)
    

if __name__ == '__main__':
     main()