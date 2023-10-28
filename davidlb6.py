def menu():
    print("Menu", "\n------------- \n1. Encode \n2. Decode"
        "\n3. Quit")

def decode(password):
    decode_list =[]
    for digit in password:
        decode_list.append(int(digit))

    ranng = len(decode_list)

    for i in range(0,ranng):
        decode_list[i] = decode_list[i] - 3

    for i in range(0,ranng):
        decode_list[i] = str(decode_list[i])

    decoded_pass = "".join(decode_list)
    print(decoded_pass)
