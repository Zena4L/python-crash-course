#username program
# Assign a unique username using first letter of first name 
# and first 4 letters of last name

def username():
    #print message
    print("---- HELLO TO MY APP------")
    # get user details
    firstName = input("Your first name : ")
    lastName = input("Your last name : ")
    # form usernam
    username = firstName[0]+lastName[:4]
    # out put uniques username
    print("---- Welcome : {} ".format(username))


username()