import math

def EOQ(A,B,C):
    eoq=math.sqrt((2*A*B)/C)

    return eoq

a=float(input("Enter annual demand of the company:"))
b=float(input("Enter the ordering cost per order:"))
c=float(input("Enter the holding cost per year:"))

e=EOQ(a,b,c)
print("The Economic Order Quantity of the company:",e)