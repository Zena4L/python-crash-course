# psuedocodes for problem

# input temperature in degree celcius
# Convert to Fahrienhiet using F=9/5C + 32
# Output results in Fahrienhiet to the screen

# author  : Clement Owireku-Bogyah

# @F = fahrienhiet , @C = celcius

def tempConv():
    print("Welcome to your temperature converter\nThis program converts from Cel of Fah\n")
    c = eval(input("Input temp in Celcius : "))
    f = (9/5)*c + 32
    print("Temp in celcius is : ",c,"ºC")
    print("Temp in Fahrinhiet is : ",f,"ºF") 
    print("Have a nice day")

tempConv()
