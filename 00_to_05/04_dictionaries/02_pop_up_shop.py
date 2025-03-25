fruits : dict = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

def total(quantity:list[int]):
   
    save_multiply = []

    count = 0
    for fruit, price in fruits.items():
        manage = quantity[count]
        count += 1
        multiply = manage * price
        save_multiply.append(multiply)
        
    total_amount = sum(save_multiply)
    print(f"\nTotal Amount = {total_amount}")


def main():
    arr : list[int] = []
    for fruit, price in fruits.items():
        user_input = int(input(f"How many {fruit} do you want to buy?:"))
        arr.append(user_input)

    total(arr)

if __name__ in  "__main__":
    main()