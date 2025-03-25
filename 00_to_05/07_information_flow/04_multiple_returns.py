def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Tuple return ho raha hai

def main():
    user_data = get_user_data()  # Tuple ko store karna
    print("\nReceived the following user data:", user_data)  # Tuple print karna

if __name__ == "__main__":
    main()
