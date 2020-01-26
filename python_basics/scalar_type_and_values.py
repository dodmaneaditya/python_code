'''
Author : Aditya Hegde
Description : Demo on Scalar Types : integer, float, string & Boolean
Date:
'''

print("\n ----------- Demo on Integer Type ------------------ \n")
a = 10
b = 0b10  #binary
c = 0o10  #octal
d = 0x10  #hexa decimal

e = int(10.5)  #decimal to int
f = int(-3.5)
g = int("105")  # from string to int

print("Integer Value: \n", a, "\n", b, "\n", c, "\n", d, "\n", e, "\n", f, "\n", g)

print("\n ----------- Demo on Floating Type ------------------ \n")
f1= 20.5
f2 = 3e4
f3 = 1.564e-20
f4 = float(10)
f5 = float("1.564")
f6 = float("nan")
f7 = float("inf")
f8 = float("-inf")
f9 = 1.5 + 1
print("\n Floating Values: \n", f1, "\n", f2, "\n", f3, "\n", f4, "\n", f5, "\n",f6, "\n", f7, "\n", f8, "\n",f9)

print("\n----Demo on None-------\n")
n1 = None # Assigns a null value
print("n1 is:")
print(n1 is None)

print("\n-----------------Demo on Bool----------------\n")
# bool() function returns either TRUE or FALSE value
b1 = bool(0)
b2 = bool(41)
b3 = bool(-19)
b4 = bool(0.0)
b5 = bool(0.3)
b6 = bool([])
b7 = bool([1,2,3])
b8 = bool("")
b9 = bool("aditya")

print("\n Boolean Values are: \n", True, "\n", False,"\n", b1, "\n",b2, "\n", b3,"\n", b4, "\n", b5, "\n", b6, "\n", b7, "\n", b8, "\n"
      , b9)