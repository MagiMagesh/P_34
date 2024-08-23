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

# will write a new data
# it will replace the old data with new data
# even if the file is not present new file will be created

with open('P_34/day11/file1.txt',mode='w') as a:
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