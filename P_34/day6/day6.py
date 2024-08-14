
# Q1. a = [1,2,'3',4,5,6,'7'] # add 5 to all these numbers

a = [1,2,'3',4,5,6,'7']

for i in a:
    print(int(i) + 5)

# Q2. a = [['Magesh','Good','1,2',345,345.456],3,4,5,['33,234,','one']]
    # need to get oo as otuput
    # need to get 345.456 as otuput

a = [['Magesh','Good','1,2',345,345.456],3,4,5,['33,234,','one']]
print(a[0])
print(a[0][1][1:3])
print(a[0][-1])

a = [[['Magesh','Good','1,2',345,345.456]],3,4,5,['33,234,','one']]
print(a[0])
print(a[0][0][1][1:3])


# str function :

# syntax:
# string_data.split('substring')
# the output will be a list
# split will break the string wherever the substring is found.
# substring will be removed.
# the element in the right the element in the left will be considered as the list element

a = 'I live in India'
b = a.split(' ') # [ 'I' , 'live' , 'in', 'India' ]
print(b)

a = 'I live in India '
b = a.split(' ') # [ 'I' , 'live' , 'in', 'India','' ]
print(b)

a = ' I live in India   '
b = a.split(' ') # [ '', 'I', 'live' , 'in', 'India','','','' ]
print(b)

a = ' I live in India   '
b = a.split() # ['I', 'live' , 'in', 'India' ]
print(b)

a = 'I67ilive67iin67iIndia'
b = a.split() # ['I67ilive67iin67iIndia' ]
print(b)

a = 'I67ilive67iin67iIndia'
b = a.split('67i') # ['I', 'live' , 'in', 'India' ]
print(b)

# list functions/ list methods

print(dir(list))

# , , 'copy', 'count', '', , , '', '', ''

# 'append'
# 'insert', 
# 'pop',
# clear empties the list check after session
# 'clear'
# 'index'
# remove - remove that element from list check after session
# extend
# count
# reverse - it will be iterator
# sort

# len() - can be used for many iterable datatype
# number of element int that datatype

a = ['I    ', 'live  ' , 'in', 'Ina876876dia' ]
print(len(a)) # 4

# append:

# syntax:
# list_data.append(any_element)

# 1. append will take only one element
# 2. this element will be added to the end of the list
# 3. this action will update the source


a = ['I', 'live' , 'in', 'India' ]
a.append('Magesh') # ['I', 'live' , 'in', 'India' , 'Magesh' ]
print(a) 

a = ['I', 'live' , 'in', 'India' ]
a.append('Magesh') 
a.append(1234) 
print(a) # ['I', 'live' , 'in', 'India' , 'Magesh' , 1234 ]

a = ['I', 'live' , 'in', 'India' ]
a.append('Magesh',123) # Error 

a = ['I', 'live' , 'in', 'India' ]
a.append(['Magesh',123]) # Error 
print(a) # ['I', 'live' , 'in', 'India',['Magesh',123] ]

# pop

# syntax:
# list_data.pop()
# list_data.pop(index_number)

# 1. by default it will remove one element at the end of the list
# 2. this action will update the source
# 3. we can use the pop out element

a = ['I', 'live' , 'in', 'India' ]
print(a.pop()) # 'India' 
print(a.pop()) # 'in' 
print(a) # ['I', 'live' ]

a = ['I', 'live' , 'in', 'India' ]
print(a.pop(2)) # 'in' 
print(a) # ['I', 'live' ,  'India' ]

# insert: # 
# list_data.insert(index_number,any_element)
# 1. insert will take only two element
# 2. this element will be inserted to the index position what we give
# 3. this action will update the source

a = ['I', 'live' , 'in', 'India' ]
a.insert(2,'Magesh') # ['I', 'live' , 'Magesh' ,'in', 'India' ]
print(a) 

a = ['I', 'live' , 'in', 'India' ]
a.insert(2,['Magesh','one']) # ['I', 'live' , 'Magesh' ,'in', 'India' ]
print(a) 


# index
# similar to str indexing
# syntax:
# list_data.index(any_element)

# 1. it will give you the index number of that element

a = ['I', 'live' , 'in', 'India' ]
print(a.index('I')) # 0


a = ['I', 'live' , 'in', 'India','1',1 ]
print(a.index(1)) # 0


a = ['I', 'live' , 'in', 'India' ]
print(a.index('Ii')) # Error


# extend

# syntax:
# list_data.extend([many_elements])

# 1. extend will take many_elements
# 2. these element will be added to the end of the list
# 3. this action will update the source

a = ['I', 'live' ]
a.extend(['1',2,3,4])
print(a) # ['I', 'live','1',2,3,4 ]


# count

# similar to str count
# syntax:
# list_data.count(any_element)

a = ['I', 'live', '1',2, '1' , 1 , 2 , 2, '1111' , '1' , 'in', 'India','1',1 ]
print(a.count(1)) # 2
print(a.count('1')) # 4