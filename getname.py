import string
from itertools import product


def getname():
    targets = string.ascii_letters  # a-z, A-z
    result = [''.join(a) for a in product(targets, repeat=3)]  # name combinations of 3 letter length
    return result


xlist = getname()

for i in xlist:
    print(i)
