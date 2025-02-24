import math

def EOQ(A,B,C):
    eoq=math.sqrt((2*A*B)/C)

    return eoq

a=float(input("Enter annual demand:"))
b=float(input("Enter the ordering cost:"))
c=float(input("Enter the holding cost:"))

e=EOQ(a,b,c)
print("The Economic Order Quantity:",e)