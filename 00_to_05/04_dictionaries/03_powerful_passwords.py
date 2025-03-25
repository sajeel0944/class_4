from hashlib import sha256

def hash_password(password:str)->str:
    return sha256(password.encode()).hexdigest()


def login(email:str, all_data:dict, password:str)-> str:
    try:
        if all_data[email] == hash_password(password):
            return ("\nlogin successfull")

        return ("\ninvalid password")
    except Exception as e:
        return ("\ninvalid email")


def main():
    login_data : dict = {
        "xyz@gmail.com" : "3608bca1e44ea6c4d268eb6db02260269892c0b42b86bbf1e77a6fa16c3c9282",
        "abc@gmail.com" : "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        "123@gmail.com" : "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    }

    user_email : str = input("Enter Your Email : ")
    user_password : str = input("Enter Your Password : ")

    if user_email and user_password:
        print(login(user_email, login_data, user_password))
    else:
        print("\nFill this")

   


if __name__ in "__main__":
    main()








