from functools import reduce

# reduce(function,iterable_data)
# function in reduce takes two inputs
# reduce will give only one input

a = [1,2,3,4,5]

c = reduce(lambda x,y: x+y,a)
print(c)
