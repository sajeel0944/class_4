import random

NUM_ROUNDS = 5  # Total kitne rounds khelenge

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Player ka score track karne ke liye

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")  # Round number print karna
        user_number = random.randint(1, 100)  # User ka random number
        computer_number = random.randint(1, 100)  # Computer ka random number

        print(f"Your number is {user_number}")

        # Valid input tak repeat karna
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break  # Valid input mila, loop exit
            print("Please enter either 'higher' or 'lower'.")

        # Game logic: User ka guess check karna
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Sahi guess pe point milega
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")  # Score show karna

    # Game ka end message
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly! 🎉")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😔")

# Game ko run karna
high_low_game()
