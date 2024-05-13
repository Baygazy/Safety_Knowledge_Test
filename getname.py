import string
from itertools import product


def getname():
    targets = string.ascii_letters
    result = product(targets, repeat=3)
    return result


xlist = getname()
print(list(xlist))
# for i in xlist:
#     print(i)
