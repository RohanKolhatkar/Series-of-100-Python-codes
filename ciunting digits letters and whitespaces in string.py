## pyhton program to count symbols ,digits, letters and whitespaces...
# symbols allowed== ( , .  ! @ # $ % ^ & * ( )   ) 

str= input("enter a string contaning digits letters synbols and whitespaces \n")
str = str.lower(); 

countdigit=0
countsymbols=0
countletter=0
for i in range(0,len(str)):
    #for counting digits
    if str[i] in ("1","2","3","4","5","6","7","8","9","0"):
        countdigit= countdigit+1
    # for counting letters
    elif (str[i] >= 'a' and str[i] <= 'z'):
        countletter= countletter +1
    # for counting symbols
    elif str[i] in (",", ".","!", "@", "#","$","%", "^", "&", "*",):
        countsymbols=countsymbols+1
    

# for counting numbers of whitespaces
white_spaces= len(str) -(countdigit+ countletter+ countsymbols)
print()
print("number of whitespaces are = ", white_spaces) 
print("number of symbols are = ",countsymbols)
print("number of digits are = ",countdigit)
print("number of letters are = ",countletter)
print()
print("    THANK YOU buddy")
print()