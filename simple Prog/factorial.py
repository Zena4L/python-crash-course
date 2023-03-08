# Specifications
# input: an interger value n
# Process : calculate the factorial of that number. n! = (n-1)(n-2) ... 1
# Output : factorial of n

# author  : Clement Owireku-Bogyah

# pseudocodes
# 1) print nice welcome
#2) accept user input.. only intergers
#3) initiate a variable fact = 1
#4) create a loop using the range of to process. range(n,1,-1)
#       - starts at n, endpoint is 1 and step is -1.


def factorial():
    print("---- Factorial Calculator -----")
    n = eval(input("Enter n (Whole numbers only) : "))
    fact = 1
    for factorial in range(n,1,-1):
        fact = fact * factorial

    print("Factorial of ",n," is", fact)

factorial()