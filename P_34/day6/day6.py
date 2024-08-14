
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

# list functions/ list methods

print(dir(list))

'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

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