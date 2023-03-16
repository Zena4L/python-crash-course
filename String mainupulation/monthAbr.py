#A program to print the month abbreviation given it number

def monthAbr():
    # a month lookup tale
    months = [
        "Jan","Feb","Mar","Apr","May",
        "Jun","Jul","Aug","Sept","Oct",
        "Nov","Dec"
    ]
    n = eval(input("Enter a Month number (1 - 12) :"))
    print("The month abbreviation is : ", months[n-1] + "." )

monthAbr()