
#TODO:
"""
You'll combine list comprehension and slicing to sample a two-dimensional data set.
You aim to create a smaller but representative sample
of data from a prohibitively large sample.
"""
##data daily stock prices  in ($)
price = [   [9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
            [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
            [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
            [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
#oneliner
sample = [line[::2] for line in price]
print(sample)