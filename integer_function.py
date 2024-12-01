import math

x = math.fsum([1.23e+18, 1, -1.23e+18])
print(x)
r = format(x, '0.2f')
print(r)
p = format(x, '>10.1f')
print(p)

swap_separators = {ord('.'): ',', ord(','): '.'}
x = format(x, ',').translate(swap_separators)
print(swap_separators)
print(x)