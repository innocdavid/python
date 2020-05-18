#TODO:
"""
Our goal is to find a particular text query within a multiline string.
We want to find the query in the text and return its immediate environment,
up to 18 positions around the found query.
"""

##Data

letter_amazon = '''
                We spent several years building our own database engine,
                Amazon Aurora, a fully-managed MYSQL and PostgrSQL-compatible
                with the same or better durability and availability as 
                the commercial engines, but at one-tenth of the cost.
                We were not surprised when this worked.
                '''

##one liner
find = lambda x, q: x[x.find(q)-18: x.find(q)+18] if q in x else -1
print(find(letter_amazon, 'SQL'))
