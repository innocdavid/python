#TODO:
"""
"""
##data
txt = ['lambda function is an anonymous function.'
        'anonymous functions dont have a name.'
        'functions are objects in Python.']

#query
q = 'anonymous'

##one_liner
mark = map(lambda s: (1, s) if q in s else (0, s), txt)

##result
print(list(mark))



