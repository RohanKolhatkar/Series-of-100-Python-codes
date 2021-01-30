
''''cube root program using guess and check '''
'''does not include approximate solutions'''

x= int(input("enter the integers"))

'''for 0 and positive integers'''
if x>=0:
    guess =0
    while guess**3 < x:
        guess = guess +1
    if guess**3  !=x:
        print("this is not a perfect cube")
    else: 
        print("cube  root is", guess)

'''for negetive integers'''

if x<0:
    guess =0
    while guess**3 > x:
        guess = guess -1
    if guess**3  !=x:
        print("this is not a perfect cube")
    else: 
        print("cube  root is", guess)





'''other method for negetive numbers by changing it to postive 
and using answer (- guess) instead of guess in print statement. '''
# if x<0:
#     x=abs(x)
#     guess =0
#     while guess**3 < x:
#         guess = guess +1
#     if guess**3  !=x:
#         print("this is not a perfect cube")
#     else: 
#         print("cube  root is", -guess)