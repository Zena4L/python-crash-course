def user(id,name,age,school):
    person = {
        'id':id,
        'name':name,
        'age':age,
        'school':school
    }
    return person

print(user(01,'clememt',23,'umat'))

def family(*fam):
    print(fam)

family('me','mother','son')

def myList(users):
    for user in users:
        print(user)

user=['sam','jonah','yaw']
myList(user)