## guess using for squre root for all values 


'''it only takes positive values and tells of perfect square only'''
x= int(input("enter the integers"))

if x>=0:
    guess =0
    while guess**2 < x:
        guess = guess +1
    if guess**2 !=x:
        print("this is not a perfect square")
    else: 
        print("square root is", guess)

else:
    print("invalid input !! aborting !!! square of negetive numbers not possible")
