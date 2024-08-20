# tuple:
# immutable data type

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

# dict: