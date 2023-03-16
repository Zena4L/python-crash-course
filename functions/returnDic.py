# this function returns a dictionary
def build_person(first_name,last_name,age = ''):
    """ This function returns a dictionary"""
    person = {'first':first_name,
              'last':last_name
              }
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrick','27')
print(musician)