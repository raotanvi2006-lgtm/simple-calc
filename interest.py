import mmath
p = int(input("enter the principle amount"))
t = int(input("enter the time"))
r = int(input("enter the rate"))
n = int(input("enter the number per year"))

si = (p*t*r)/100
print("simple interest is:",si)
ci = p* math.pow((1+(r/(100*n))),n*t)
print("compound Interest is:",ci)
