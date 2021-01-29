
x=int(input("\n enter a number whose square root is to found \n"))
if x<0:
    print("square root of negetive numbers not possible as square's cannot be negetive  ABORTING !! ")

if x ==0:
    print("it's square root is 0")

if x>0:
    epsilon = 0.1
    guess=0
    increment=0.01
    num_guess=0
    while abs(guess**2 - x) >= epsilon:
        guess= guess+ increment
        num_guess+=1

    if abs(guess**3 - x) >= epsilon:
        print("failed on square root of :\n", guess)
    else:
        print("square root is close to \n", guess)

    print()
    print("number of guesses taken =" , num_guess)
