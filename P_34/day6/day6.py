
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


# 'append'
# 'insert', 
# 'pop',
# clear empties the list check after session
# 'clear'
# 'index'
# remove - remove that element from list check after session
# extend
# count
# reverse 
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


a = ['I', 'live' , 'in', 'India','1',1 ]
print(a.index(1)) # 5 

# reverse a string
a = 'I live in India'
print(a[::-1]) # 'aidnI ni evil I'

# reverse a list
a = ['I', 'live' , 'in', 'India','1',1 ]
print(a[::-1]) # [1, '1','India','in','live' ,'I']


# reverse

# syntax:
# list_data.reverse()

# 1. source will get changed. source i.e list_data

a = ['I', 'live' , 'in', 'India','1',1 ]
a.reverse()
print(a)

# sort

# syntax:
# list_data.sort()

# 1. source will get changed. source i.e list_data
# 2. in list all the elements should be either int+float | str

a = [11,11.1,23,23432,435,12,634]
a.sort()
print(a)

a = [11,23,'23432',435,12,634]
a.sort() # Error
print(a)


a = ['a','ac','aaa','ab','aa','AA','AB']
a.sort() # Lexicographic order || ascii value
print(a) # ['AA','AB','a','aa','aaa','ab','ac']

print(ord('a')) # 65
print(ord('z')) # 122
print(ord('A')) # 97
print(ord('Z')) # 90
print(ord('-'))
print(chr(65)) # A
print(chr(97)) # a

# sorted()

# 1. this will not update the source.
# 2. this will give us the new output

a = ['a','ac','aaa','ab','aa','AA','AB']
b = sorted(a)

print(a)
print(b)

a = [11,23,23432,435,12,634,11.1]
a.sort()
print(a)
print(a[::-1])


# it is used to avoid call by reference

a = 10
b = 15
a = a + 5
print(a)
print(b)

# call by value

a = 10
b = a
a = a + 5
print(a) # 15
print(b) # 10

# call by value
# int
# float
# str

# copy()
# we will use copy to avoid call by reference to list

# call by reference - same memory will be allocated
# list

a = [1,2,3,4,5]
b = a
a.append(6)
b.append(16)
print(a) # [1,2,3,4,5,6,16]
print(b) # [1,2,3,4,5,6,16]

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
b.append(16)
print(a) # [1,2,3,4,5,6]
print(b) # [1,2,3,4,5,16]

print('one'+'two') # 'onetwo'
print([1,2,3] + [4,5,6]) # [1,2,3,4,5,6]

print('magesh' * 3) # that string will be dupilcated to n no of times
# mageshmageshmagesh

print(['magesh'] * 3) # that string will be dupilcated to n no of times
# ['magesh','magesh','magesh']

# Q1. a = [1,'123','magesh',345,'phone','11',234.234,'zer','Earth','Moon','Mars'] the output should be
# 6
# 128
# 349
# 16
# 239.234

# Q2. a = 'i live in India'
# count of all the elements in a
# ex: 'i' is repeated for 5 times
# ex: 'l' is repeated for 4 times
# ex: ' ' is repeated for 4 times

# Q3. 
# n = 7
# *
# **
# ***
# ****
# *****
# ******
# *******

# Q4.
# n = 5
#     *
#    **
#   ***
#  ****
# *****