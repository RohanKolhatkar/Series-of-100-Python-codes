
'''PROGRAM TO FIND NUMBER OF VOWELS AND CONSONANTS AND WHITESPACES IN A GIVEN STRING'(UPPERCASE AND LOWERCASES BOTH '''




vcount = 0
ccount = 0  
str = "ROHAN IS A GOOD BOY"
   
#Converting entire string to lower case to reduce the comparisons  
str = str.lower();  
for i in range(0,len(str)):   
    #Checks whether a character is a vowel  
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1;  


print("Total number of vowel and consonant and whitespaces are" );  
print(vcount)  
print(ccount)

# for counting numbers of whitespaces
white_spaces= len(str) -(vcount + ccount)
print(white_spaces) 



