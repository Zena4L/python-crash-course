# this output a date format

def dateConv():
    # input date string in mm/dd/yy format
    dateStr = input("Enter date in the format (mm/dd/yy) : ")
    monthStr,dayStr,yearStr = dateStr.split("/")

    # we evaluate a monthly string
    months = [
        "Jan","Feb","Mar","Apr","May",
        "Jun","Jul","Aug","Sept","Oct",
        "Nov","Dec"
    ]
    monthStr = months[int(monthStr) - 1]

    # output the result in the format we want
    print("The converted date is : {0} {1},{2}".format(monthStr,dayStr,yearStr))

    # print(monthStr,dayStr,yearStr)


dateConv()