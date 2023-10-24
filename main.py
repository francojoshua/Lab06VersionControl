def encode(string: str):
    encoded_pass = ""

    for n in list(string):
        value = str(int(n) + 3)
        encoded_pass += (value if len(value) == 1 else value[-1])

    return encoded_pass


def decode(string: str):
    decoded_pass = ''
    for digit in str:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_pass += decoded_digit
    return decoded_pass

def main():
    password = ""

    while True:
        print("Menu")
        print("-------------")
        print("\n".join(["1. Encode", "2. Decode", "3. Quit"]))

        option = input("\nPlease enter an option: ")

        if option == "1":
            decoded_pass = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

            password = encode(decoded_pass)
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
        elif option == "3":
            break
        else:
            print("Invalid input")

        print()


if __name__ == "__main__":
    main()
