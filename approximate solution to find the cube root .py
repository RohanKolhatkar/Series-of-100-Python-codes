

x=int(input("\n enter a number whose cube root is to found \n"))

epsilon = 0.1
guess=0
increment=0.01
num_guess=0

if x>=0:
    while abs(guess**3 - x) >= epsilon:
        guess= guess+ increment
        num_guess+=1

    if abs(guess**3 - x) >= epsilon:
        print("failed on cube root of :\n", guess)
    else:
        print("cube root is close to \n", guess)

    print()
    print("number of guess = ", num_guess)
    



if x<0:
    y= -x
    while abs(guess**3 - y) >= epsilon:
        guess= guess+ increment
        num_guess+=1

    if abs(guess**3 - y) >= epsilon:
            print("failed on cube root of :\n", -guess)
    else:
            print("cube root is close to \n", -guess)

    print()
    print("number of guess = ", num_guess)
 

