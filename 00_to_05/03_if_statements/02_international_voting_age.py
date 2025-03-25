PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def manage(user_age:int):
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}")
    
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}")
    
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}")

def main():
    try:
        user_input : int = int(input("How old are you? "))
        manage(user_input)
    except ValueError:
        print("Enter Only Number")

if __name__ in "__main__":
    main()