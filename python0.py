#TODO:
"""
Writing a python program that counts up 
the number of vowels in a string s.
Valid vowels are 'a', 'e', 'i', 'o' and 'u'.
such that  if s = 'azcbobobegghakl', the program should 
say that, 'the number of vowels is 5'
"""

string0 = 'azcbobobegghakl'
count = 0
for vowel in string0:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count += 1

print('The number of vowels is : ', count)




#TODO:
"""
Using multiple if statements and a for loop
"""
string1 = 'azcbobobegghakl'
count = 0
vowels = 0
for i in string1:
    if i == 'a':
        vowels += 1
    elif i == 'e':
        vowels += 1 
    elif i == 'i':
        vowels += 1 
    elif i == 'o':
        vowels += 1 
    elif i == 'u':
        vowels += 1 
    else:
        count += 1 
print('the number of vowels in the string is: ',vowels)



#TODO:
"""
Using while loop to find the number of vowels in the string
"""
string2 = 'azcbobobegghakl'
count = 0
vowels = 0
while count < len(string2):                    
    char = 0
    if string2[count] == 'a':
        char += 1 
    elif string2[count] == 'e':
        vowels += 1 
    elif string2[count] == 'i':
        vowels += 1 
    elif string2[count] == 'o':
        vowels += 1 
    elif string2[count] == 'u':
        vowels += 1
    else:
        char += 1
    count += 1 
    
print('the number of vowels in the string is: ',vowels)
