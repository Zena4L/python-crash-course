def greet_users(username):
    """ This function accepts a list of users"""
    for name in username:
        msg = "Hello {0}, Welcome !".format(name).title()
        print(msg)

username = ['clement','ty','jay']
# greet_users(username)

def make_pizza(*toppings):
    print(toppings)

make_pizza('a','b','c')