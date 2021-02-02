
print("NOTE:--->> PLEASE INPUT DISTINCT VALUES ONLY......")

x= int(input("enter the number 01: \n "))
y= int(input("enter the number 02: \n"))
z= int(input("enter the number 03: \n"))


if x>y and x>z:
    if y>z:
        print("the ascending order of numbers is :\n", z,y,x)
    else:
         print("the ascending order of numbers is :\n", y,z,x)

if y>x and y>z:
    if x>z:
        print("the ascending order of numbers is :\n", z,x,y)
    else:
        print("the ascending order of numbers is :\n",x,z,y)

if z>x and z>y:
    if x>y:
        print("the ascending order of numbers is :\n", y,x,z)
    else:
        print("the ascending order of numbers is :\n", x,y,z)

print("your WORK is done.......")