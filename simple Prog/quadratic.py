# Specifications
# input: Accept 3 values, coeffiecint of a,b,c
# Process : solve the quadratic
# Output : two values for x.

import math

def quadratic():
    print("Declaimer : Values should be b*b -4ac < 0")
    a,b,c = eval(input("Enter coeffieceint of a,b,c : "))
    diskRoot = math.sqrt(b*b - 4*a*c)
    root1 = (-b + diskRoot)/ 2*a
    root2 = (-b - diskRoot)/ 2*a

    print("x1 : ",root1,"\nx2",root2)


quadratic()