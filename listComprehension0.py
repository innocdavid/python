
#TODO:
"""
A Dictionary containing the names of employees
and their respective amount of salaries.

Writing a python program that determines the
employees with salaries above 100000
"""

#Create a dictionary of employee salaries
employees = { 'Alice' : 100000,
              'Bob' : 99817,
              'Carol' : 122908,
              'Frank' : 88429,
              'Eve' : 93121}
#Who are the top earners getting over
#100k per month?
top_earners = []
for key, value in employees.items():
    if value >= 100000:
        top_earners.append((key, value))

#printing the values
print('The list of top earners include:  \n',top_earners)

"""
Using one liner to manipulate the list of 
top earners and append the names and salaries into the list.
"""

#Create a dictionary of employee salaries
employees = { 'Alice' : 100000,
              'Bob' : 99817,
              'Carol' : 122908,
              'Frank' : 88429,
              'Eve' : 93121}
#Who are the top earners getting over
#100k per month?
top_earners = [(key, value) for key, value in employees.items() if value == 100000]

#printing out the result
print(top_earners)



    


