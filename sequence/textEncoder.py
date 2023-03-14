# this program enocode text to it ASCII values

def encoder():
    # get message from user
    message = input(" message : ")

    for ch in message:
        print(ord(ch), end=" ")

encoder()

