user_0 = {
    'firstN':'Clement',
    'middleN':'Owireku',
    'lastN':'Bogyah'
}
# the key here is assign to values and then .item() method is added to the dictionary identifier
for key,value in user_0.items():
    print(key.rstrip()+" " + ":" +" "+ value.lstrip())
# use key() method to loop through keys
print("-------------------")
for key in user_0.keys():
    print(key)

print("-----------------")
for key in sorted(user_0.keys()):
    print(key.upper() + " "+"Thank you")

print("--------------")
#values() method is used to loop through values
for values in user_0.values():
    print(values.title())