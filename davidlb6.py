github = ''
def encode(password):
    encode_list = []
    for digit in password:
        encode_list.append(int(digit))

    for i in range(0,len(encode_list)):
        number = encode_list[i] + 3
        if number >= 10:
            number =- 10

        encode_list[i] = number


    for j in range(0, len(encode_list)):
        encode_list[j] = str(encode_list[j])

    enc = "".join(encode_list)
    global github
    github = enc
    print("Your password has been encoded and stored!")
    return github

def menu():
    print("Menu", "\n------------- \n1. Encode \n2. Decode"
        "\n3. Quit")

def decode(password):
    decode_list =[]
    for digit in password:
        decode_list.append(int(digit))

    ranng = len(decode_list)

    for i in range(0,ranng):
        number = decode_list[i] - 3
        if number < 0:
            number = decode_list[i] - 3 + 10

        decode_list[i] = number

    for i in range(0,ranng):
        decode_list[i] = str(decode_list[i])

    decoded_pass = "".join(decode_list)
    print("The encoded password is",password, "and the original password is", decoded_pass)




menu()
menu_option = int(input("Please enter an option:"))

while True:
    if menu_option == 1:
        password = input("Please enter your password to encode:")
        encode(password)
        menu()
        menu_option = int(input("Please enter an option:"))

    elif menu_option == 2:
        decode(github)
        menu()
        menu_option = int(input("Please enter an option:"))

    elif menu_option == 3:
        exit()

if __name__ == '__main__':
    main()










