# this function has a keyword arguement

def describe_pet(animal_type,pet_name = "harry",pet_age = "1.2"):
    """ This describe animal type and it's name """
    print('I have {0}'.format(animal_type))
    print("My {0}'s name is {1} and it's {2} years".format(animal_type,pet_name.title(),pet_age))

describe_pet(animal_type='hamster',pet_age='2')

