# tuple:
# immutable data type
() # empty tuple
print(tuple()) # ()
print(list()) # []

# 1. almost similar to list
# 2. indexing & slicing similar to list

a = (1,2,3,4,5,6,'Magesh',[1,2,3,4])
print(a[-1][1])

# tuple does not support item assignement
a = (1,2,'Magesh',[1,2,3,4])
a[4] = 15
print(a)

a = (1,2,'Magesh',[1,2,3,4,'lotus'])
for i in a:
    print(i)

# 1
# 2
# Magesh
# [1,2,3,4,'lotus']

print(dir(tuple))

# 'count', 'index' - both functions are similar to list

a = (1,2,3,1,2,3,2,2,2,2,4,'Magesh',[1,2,3,4,'lotus'])
print(a.count(1)) # 2
print(a.count(2)) # 6
print(a.index(2)) # 1

a = (1,'Magesh',[1,2,3,4,'lotus'])
print(len(a)) # 3
print(type(a)) # <class 'tuple'>

a = ('I', 'live' , 'in', 'India','1',1 )
print(a[11]) # error tuple index out of range

a = 'Magesh'
b = list(a) # ['m','a','g','e','s','h']
print(b)

a = (1,2,3,1,2,3,2)
b = list(a) # [1,2,3,1,2,3,2]
print(b)


a = [1,2,3,1,2,3,2]
b = tuple(a) # (1,2,3,1,2,3,2)
print(b)

a = 'Magesh'
b = tuple(a) # ('M','a','g','e','s','h')
print(b)


a = ('M','a','g','e','s','h')
b = str(a)  #       "('M','a','g','e','s','h')"
print(b)    #       "('M','a','g','e','s','h')"
print(b[0]) # (

# str <=> tuple <=> list

# set:
# collection of unordered datatype

# set does not support indexing

print(set()) # set()

# 1. set will have only unique elements

a = {1,1,1,1,2,2,2,3,1,2,3,12,3,2,4,23,4,2,342,3,4,23,421,3,12,32,34,3,4}
print(a)

a = {123,11,1,2,34,3,4}
print(a)

# any iterable data type can be converted into set

a = [123,11,1,2,34,3,4,4,4,4,2,2,3,5]
b = set(a)
print(b)

a = {123,11,[1,2,34,3],4,4,4,4,2,2,3,5} # error
a = {123,11,{1,2,34,3},4,4,4,4,2,2,3,5} # error
a = {123,11,(1,2,34,3),4,4,4,4,2,2,3,5} 
a = {123,11,(1,[2,34],3),4,4,4,4,2,2,3,5} # error

print(dir(set))

#  'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

a = {1,2,3,4,5}
a.add(56)
a.add(565)
a.add(5)
print(a)

# similar to copy in list.
# it is used to avoid call by reference.

# pop will remove the random element
a = {1,1,1,1,2,2,2,3,1,2,3,12,'3',2,4,23,4,2,'342',3,4,23,421,3,12,32,34,3,4}
print(a)
print(a.pop())
print(a)

# remove will remove the random element
a = {1,1,1,1,2,2,2,3,1,2,3,12,3,2,4,23,4,2,342,3,4,23,421,3,12,32,34,3,4}
print(a)
a.remove(2)
a.remove(421)
print(a)

a = {1,2,3,4,5}
a.update([56,1,2,23,4,234,23,543,46])
a.update((123,234,345))
a.update({1243,2344,3445})
print(a)

a = {1,2,3,4,5}
b = {5,4,6,7,8}
c = a.union(b) # {1, 2, 3, 4, 5, 6, 7, 8}
d = a.intersection(b) # {4,5}
e = a.difference(b) # only elements of A {1,2,3}
ee = b.difference(a) # only elements of B {6,7,8}
f = a.symmetric_difference(b) # only elements of A {1,2,3} + only elements of B {6,7,8}
a.difference_update(b) # # only elements of A {1,2,3} will get updated to a

a = {1,2,3,4,5}
b = {5,4,6,7,8}
a.symmetric_difference_update(b)
print(a) # {1,2,3,6,7,8}

print(c)
print(d)
print(e)
print(ee)
print(f)
print(a)


a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {1,2,3,4,5}
print(a.issuperset(b)) #  whether lemenet a contains all the elements of B
print(b.issuperset(a)) 
print(b.issubset(a)) # Whether all the elements of B present in A or not
print(a.issubset(b))  



# dict:

