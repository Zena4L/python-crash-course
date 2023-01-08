user_0 = {
    'firstN':'Clement',
    'middleN':'Owireku',
    'lastN':'Bogyah'
}
# the key here is assign to values and then .item() method is added to the dictionary identifier
for key,value in user_0.items():
    print(key.rstrip()+" " + ":" +" "+ value.lstrip())