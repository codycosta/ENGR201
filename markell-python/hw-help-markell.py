
# grab integer values
a, b, c, d, e, f = input('enter 6 whole numbers with spaces between each entry: ').split()
print(a, type(a), '\n')   # type check


# grab float values
g, h, i = input('enter 3 numbers to 3 decimal points with spaces between each entry: ').split()
print(g, type(g), '\n')   # type check


# check all values are correct
print(a, b, c, d, e, f, g, h, i, '\n')


# calculate result
result =  round( (((int(a)**int(b) + int(c) * int(d) - int(e))/int(f)) % float(g)) + float(h) - float(i), 3 )
print(result)
