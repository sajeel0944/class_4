user_adjective: str = input("Please type an adjective and press enter. ")
user_noun: str = input("Please type a noun and press enter. ")
usr_verb: str = input("Please type a verb and press enter. ")

def main(adjective:str, noun:str, verb:str):
    print(f"I saw a {adjective} {noun} that was {verb} down the street!")

if __name__ in "__main__":
    main(user_adjective, user_noun, usr_verb)