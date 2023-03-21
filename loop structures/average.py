# find the average of numbers
# using sentinel values

def main():
    # n = eval(input("How many numbers do you want : "))
    # sum = 0.0

    # for i in range(n):
    #     x = eval(input("Enter X: "))
    #     sum = (sum + x)/n
    # print("sum = {0}".format(sum))
    sum = 0.00
    count = 0
    x = eval(input("Enter a number (negative number to quit ) >> "))
    while x >= 0:
        sum = sum + x
        count= count+1
        x = eval(input("Enter a number (negative number to quit ) >> "))
    print("average = ",sum/count)


if __name__:
    main()

