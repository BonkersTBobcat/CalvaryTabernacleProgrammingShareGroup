import json

encryption_key = ""
shift_cipher = 0

with open("Program8_encryption_keys.json") as f:
    data = json.load(f)
    encryption_key = data["key"]
    shift_cipher = int(data["shift"])

def encrypt_shift(plaintext):
    value = ""
    for character in plaintext:
        value += chr(ord(character) + shift_cipher)
    return value

def encrypt_shift_key(plaintext):
    value = ""
    index = 0
    for character in plaintext:
        value += chr(ord(character) + ord(encryption_key[index]))
        index += 1
        if index>=len(encryption_key):
            index=0
    return value

def decrypt_shift(plaintext):
    value = ""
    for character in plaintext:
        value += chr(ord(character) - shift_cipher)
    return value

def decrypt_shift_key(plaintext):
    value = ""
    index = 0
    for character in plaintext:
        value += chr(ord(character) - ord(encryption_key[index]))
        index += 1
        if index>=len(encryption_key):
            index=0
    return value

while True:
    option = input("Would you line to encrypt (E) or decrypt (D): ").lower()
    file_mode = input("Would you like to use file mode (Y/N): ").lower() == "y"
    # encrypt mode
    if option == "e":
        # get message
        if file_mode:
            filepath = input("Please enter file path: ")
            with open(filepath, "r") as f:
                message = f.read()
        else:
            message = input("Please enter message: ")
        # encrypt message
        message = encrypt_shift(message)
        message = encrypt_shift_key(message)
        # output message
        if file_mode:
            with open(filepath, "w") as f:
                f.write(message)
        else:
            print(message)
    # decrypt mode
    elif option == "d":
        # get message
        if file_mode:
            filepath = input("Please enter file path: ")
            with open(filepath, "r") as f:
                message = f.read()
        else:
            message = input("Please enter message: ")
        # decrypt message
        message = decrypt_shift_key(message)
        message = decrypt_shift(message)
        # output message
        if file_mode:
            with open(filepath, "w") as f:
                f.write(message)
        else:
            print(message)
        print(message)
    elif option == "q":
        break
    else:
        print("NOT A VALID OPTION")