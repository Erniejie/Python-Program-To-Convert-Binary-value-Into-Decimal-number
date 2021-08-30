#Python-Program To Convert Binary value Into Decimal number
"Computer Programming Tutor, Aug 30,2021"

def binaryToDecimal(no):
    a = no
    sumd = 0
    i = 0
    n = 0
    while(no != 0):
        dec = no % 10
        sumd = sumd + dec*pow(2,i)
        no = no // 10
        i += 1
    print(sumd)
        
no = int(input("Enter an Binary Number: "))
print("The Equivalent Decimal Number is: ",end="")
binaryToDecimal(no)
