#TODO:
"""
Writing a program that reads a file and
stips off the leading and trailing whitespaces
in the file and store everything in a list of
strings
"""

#Code to read the file
filename = 'listComprehension0.py'

f = open(filename)
lines = []

for i in f:
    lines.append(i.strip())

print(lines)


#TODO:
"""
Putting in a single line of code
"""

print([i.strip() for i in open('listComprehension1.py') ])

