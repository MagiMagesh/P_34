a = '12313234234234'
from functools import reduce
c = reduce(lambda x,y: int(x)+int(y),a)
print(c)