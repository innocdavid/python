#TODO:
"""
Writing a program that prints the number of times the string 
'bob' occurs in variable s.
For example, if s = 'azcbobobegghakl', then your 
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
count = 0
for x in range(len(s)):
    if s[x:x+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))



#TODO:
"""
Using a while loop to print the same program
"""
name = 'azcbobobegghakl'
count = 0
x = 0
while x < len(name):
    if name[x:x+3] == 'bob':
        count += 1 
    x += 1
print('Number of times bob occurs is:',count)