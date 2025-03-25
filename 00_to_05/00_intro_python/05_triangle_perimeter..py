try:
    side_1 : float = float(input("What is the length of side 1 : "))
    side_2 : float = float(input("What is the length of side 2 : "))
    side_3 : float = float(input("What is the length of side 3 : "))

    def main(side_no_1:float, side_no_2:float, side_no_3:float):
        print("\n")
        print(f"Frist side of triangle : {side_no_1}")
        print(f"Second side of triangle : {side_no_2}")
        print(f"Third side of triangle : {side_no_3}")

        print(f"\nThe perimeter of the triangle is : {side_no_1 + side_no_2 + side_no_3}")

    if __name__ in "__main__":
        main(side_1, side_2, side_3)

except ValueError :
    print("\nPlease enter only number")
