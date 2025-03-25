def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        user_input = input("Please type the following affirmation:\n" + affirmation + "\n\n")
        
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm, that was not the affirmation. Try again.\n")

if __name__ == "__main__":
    main()
