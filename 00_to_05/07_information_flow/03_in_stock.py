from typing import Dict

def num_in_stock(fruit:str) -> int:
    inventory : Dict[str,int]= {
        "apple": 50,
        "banana": 120,
        "pear": 1000,
        "orange": 200,
        "grape": 0, 
    }

    return inventory.get(fruit,0)

def main():
    user_input : str = input("Enter a fruit: ")
    convert_lower = user_input.lower()
    if user_input == "":
        print("please enter fruit name")
    else:
        save_data = num_in_stock(convert_lower)
        print(save_data)

if __name__ in "__main__":
    main()
