import secrets

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"

all_characters = letters + numbers + symbols
no_letters = numbers + symbols
no_numbers = letters + symbols
no_symbols = letters + numbers

length = int(input("Enter the desired password length: "))
if length < 8:
    print("password should be at least 8 characters long.")
else:
    include_letters = input("Include letters? (y/n): ")
    include_numbers = input("Include numbers? (y/n): ")
    include_symbols = input("Include symbols? (y/n): ")

def generate_password(length, include_letters, include_numbers, include_symbols):
    password = ""
    if include_letters.lower() == "y" and include_numbers.lower() == "y" and include_symbols.lower() == "y":
        password = "".join(secrets.choice(all_characters) for _ in range(length))
    elif include_letters.lower() == "y" and include_numbers.lower() == "y":
        password = "".join(secrets.choice(no_symbols) for _ in range(length))
    elif include_letters.lower() == "y" and include_symbols.lower() == "y":
        password = "".join(secrets.choice(no_numbers) for _ in range(length))
    elif include_numbers.lower() == "y" and include_symbols.lower() == "y":
        password = "".join(secrets.choice(no_letters) for _ in range(length))
    elif include_letters.lower() == "y":
        password = "".join(secrets.choice(letters) for _ in range(length))
    elif include_numbers.lower() == "y":
        password = "".join(secrets.choice(numbers) for _ in range(length))
    elif include_symbols.lower() == "y":
        password = "".join(secrets.choice(symbols) for _ in range(length))
    else:
        return "invalid request."
    return password

generated_password = generate_password(length, include_letters, include_numbers, include_symbols)
print("Generated password:", generated_password)
