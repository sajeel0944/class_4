C : int = 299792458

user_input : float = float(input("Enter kilos of mass : "))

def main(m:float):
    formula = m * (C ** 2)
    print("\nFormula : e = m * C^2")
    print(f"m = + {m} + kg")
    print(f"C = C + m/s")
    print(f"{formula} joules of energy!")

if __name__ in "__main__":
    main(user_input)