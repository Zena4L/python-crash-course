# this program enocode text to it ASCII values

# def encoder():
#     # get message from user
#     message = input(" message : ")

#     for ch in message:
#         print(ord(ch), end=" ")

# encoder()


def decoder():
    code = [input("Enter code : ")]
    message = [int(x) for x in code]

    for i in message:
        print(i)
        # print(type(i))
decoder()