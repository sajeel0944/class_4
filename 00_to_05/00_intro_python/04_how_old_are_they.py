try:
    anton_age : int = int(input("Anton enter your age : "))

    def main(anton_age_value:int):
        Anton : int = anton_age_value
        Beth : int = 6 + Anton
        Chen : int = 20 + Beth
        Drew : int = Chen + Anton
        Ethan : int = Chen

        print(f"Anton age is {Anton}")
        print(f"Beth age is {Beth}")
        print(f"Chen age is {Chen}")
        print(f"Drew age is {Drew}")
        print(f"Anton age is {Ethan}")



    if __name__ in "__main__":
        main(anton_age)

except Exception as e:
    print("\nEnter only number")
