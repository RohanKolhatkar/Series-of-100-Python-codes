
# python program to find the number of uppercases and lowercase in strings.

'''using a function call method'''

a= input("enter a string")


def abst(str):
    uppercase=0
    lowercase=0
    for x in str:
        if x.isupper():
            uppercase+=1
        elif x.islower():
            lowercase+=1
        else:
            pass
    print(uppercase)
    print(lowercase)
abst(a)

'''using conditionals''' 

a= input("enter a string")

uppercase=0
lowercase=0
for x in a:
    if x.isupper():
        uppercase+=1
    elif x.islower():
        lowercase+=1
    else:
        pass
print(uppercase)
print(lowercase)