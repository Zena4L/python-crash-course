# Using chr function, we decode an ASCII number to it character

# Algo
def decoder():
        
    # Get sequence of ASCII values from users as a big string
    inString = input("Enter values here : \n")
    # Declare an empty message string
    message = ""
    # loop through each substring and build a unicode value
    for string in inString.split():
        decoded = eval(string) #convert to digit
        message = message + chr(decoded)
    # print message
    print(message)

decoder()

