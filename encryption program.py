# Write a Program to Encrypted and Decrypted Messages

def encryptor(chars, keys):

    print()
    print             ("*************************")
    plain_text = input("Write the Original text: ")
    print             ("*************************")
    print()

    cipher_text = ""

    for letter in plain_text:

        if letter in chars:

            index = chars.index(letter)
            cipher_text += keys[index]

        else:
            cipher_text += letter

    print()
    print("*****************************************")
    print(f"Your Encryted Messages is :{cipher_text}")
    print("*****************************************")
    print()


def decryptor(chars, keys):

    print()
    print              ("*************************")
    cipher_text = input("Write the Encryted text: ")
    print              ("*************************")
    print()

    plain_text = ""

    for letter in cipher_text:

        if letter in keys:

            index = keys.index(letter)
            plain_text += chars[index]

        else:
            plain_text += letter

    print()
    print("****************************************")
    print(f"Your Decryted Messages is :{plain_text}")
    print("****************************************")
    print()


def main():

    import string
    import random

    chars = " " + string.digits + string.punctuation + string.ascii_letters
    chars = list(chars)

    keys = chars.copy()
    random.shuffle(keys)

    print()
    print("***********************************************")
    print("  Welcome to Python Encrytor/Decrtyor Program  ")
    print("***********************************************")
    print()

    while True:

        encryptor(chars, keys)

        print()
        print      ("*******************************************************")
        ask = input("Do you Want to Decryted the Message? (Y/N): ").lower()
        print      ("*******************************************************")
        print()

        if ask == "y":

            decryptor(chars, keys)

            print()
            print      ("********************************************************")
            ask2 = input("Do you Want to Encryted the Message? (Y/N): ").lower()
            print      ("********************************************************")
            print()

        else:
            break

        if ask2 == "y":
            continue

        else:
            break

    print()
    print("*******************************")
    print("Thank You for Using our Program")
    print("*******************************")
    print("Don't Forget to drop a Review  ")
    print("*******************************")
    print()


if __name__ == "__main__":
    main()