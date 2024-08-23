a = [1,2,3,4,5]
b = '56789'
[5,12,21,32,45]
d = [a[i]*int(b[i]) for i in range(len(a))]
print(d)

# set comphrension 
a = [1,2,3,4,5]
b = '56789'
[5,12,21,32,45]
d = {a[i]*int(b[i]) for i in range(len(a))}
print(d)


# dict comphrension 
a = [1,2,3,4,5]
b = '56789'
# {1:'5',2:'6',...}
d = {a[i]:b[i] for i in range(len(a))}
print(d)


# FILE HANDLING:

# open

a = open('P_34/day11/file.txt')
# P_34/day11/file.txt
# /Users/magesh/Magesh/GUVI WORK/GUVI/Session/P_34/P_34/day11/file.txt
print(a)
b = a.read()
print(b)
for i in b:
    print(i)
print('taking data in memory',b)

b = a.read()
print('2nd time reading',b)

a.close()

# context manager
with open('P_34/day11/file.txt') as a:
    b = a.read()
print(b)

with open('P_34/day11/file.txt',mode='r') as a:
    b = a.read()
print(b)

with open('P_34/day11/file1.pdf',mode='r') as a:
    b = a.read()
print(b)

# will write a new data
# it will replace the old data with new data
# even if the file is not present new file will be created

with open('P_34/day11/file1.txt',mode='w') as a:
    a.write('this is new data\n')
    a.write('it will be joined with the old data\n')
    a.write('it is again it will be joined with the old data')

with open('P_34/day11/file1.pdf',mode='w') as a:
    a.write('this is new data\n')
    a.write('it will be joined with the old data\n')
    a.write('it is again it will be joined with the old data')



# it will get appended with the old data
# it will replace the old data with new data
# even if the file is not present new file will be created
with open('P_34/day11/file.txt',mode='a') as a:
    a.write('\nim magesh i live in India')
    
with open('P_34/day11/file.txt',mode='a') as a:
    b = a.read()
print(b)


# Error HANDLING: / exception handling

# try:
#     logics
# except:
#     logics

# 1. try block will handle error.
# 2. when there is error in try block in that line try block will break
# 3. except block will get executed.
# 4. except block cannoct handle error.
# 5. if there is no error in try block except will not get executed.


print('5' + 10)
print(int('234s'))


a = input("Enter Your age: ")
print(int(a))
print('Magesh')

try:
    a = input("Enter Your age: ")
    print(int(a))
    print('Magesh')
except:
    print('Please enter only number')

print('Magesh outside try block')

try:
    print('all good')
    print('Magesh')
except:
    print('There is some error')

print('Not')


try:
    print('all good')
    print('Magesh')
    print(int('234 324'))
except:
    print('There is some error')

print('Not')


try:
    if 4 > 5:
        print(1)
    if 'Magesh' * '':
        print(2)
    else:
        print(3)
    b = '123456'
    print(b[6])
    print(int('1234'))
    print(list('1234'))
    print(int('9876'))
except:
    print('thre was error')


# else:
# finally

try:
    logic
except:
    logic
else:
    logic
finally:
    logic


try:
    if 41 > 5:
        print(1)
    if 'Magesh' * '':
        print(2)
    print(list('1234'))
    print(int('9876'))
except:
    print('thre was error')
else:
    print('''if there is no error in try else will also get executed. 
          if not else will not get executed''')


try:
    if 41 > 5:
        print(1)
    print(list('1234'))
    print(int('9876'))
except:
    print('thre was error')
else:
    print('''if there is no error in try else will also get executed. 
          if not else will not get executed''')
    
try:
    if 41 > 5:
        print(1)
    print(list('1234'))
    print(''* '')

    print(int('9876'))
except:
    print('thre was error')
else:
    print('''else got executed''')
finally:
    print('always finally will get executed')


try:
    if 41 > 5:
        print(1)
    print(list('1234'))
    print(''* '')

    print(int('9876'))
except:
    print(''* '')
    print('thre was error')

print('hi this is Magesh')

try:
    try:
        if 41 > 5:
            print(1)
        print(list('1234'))
        print(''* '')

        print(int('9876'))
    except:
        print(''* '')
        print('thre was error')
    finally:
        print('THere was an emergency')
except:
    print('there was new error')
    
print('hi this is Magesh')



# any & all

# any:

a = [0,1,2,3,4,5]
print(any(a))
# If any one element in that Iterable data-type is true The output will be true

a = (False,False)
print(any(a))

a = (False,False)
print(any(a))

# all:
# If any all element in that Iterable data-type is true The output will be true

a = [0,1,2,3,4,5]
print(all(a)) # False

a = [1,2,3,4,5]
print(all(a)) # True



# break continue
# must be used only in the iteration.


# pass:
# to compelete a statement
# it will not included in coding part.

if True:
    pass

def custom_funciton():
    pass



# continue:
# 1. it skip that particular iteration
# anything below to continue will not be executed

a = [1,2,3,4,5]
for i in a:
    if i == 3:
        continue
    print(i)


a = [1,2,3,4,5]
for i in a:
    print(i)
    pass
    if i == 3:
        continue
    else:
        pass

# break:
# 1. it terminated that particular iteration/loop

a = [1,2,3,4,5]
for i in a:
    print(i)
    pass
    if i == 3:
        break
    else:
        pass

# break

a = [1,2,3,'Mages',5,6,[1,2,3],'Jamine',8,'9',23.234,(1,3,4),{1,2,3},{1:1,2:2,3:3}] 

for i in a:
    print(i)
    if type(i) == str:
        continue
    if type(i) == list:
        break
    print(2*i)
    print(10*'-')

a = [1,2,3,4,5,6,7]
b = [11,12,13,14]

for i in b:
    # print(i)
    for j in a:
        print(j*i)
    print(10 * '-')

# iter & generator