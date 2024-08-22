

# print()
print(print(4))
print(print())


def  addition(data):                
    b = 0
    for i in data:
        b = b + i
    print(b)

a = [1,2,3,4,5,6,7,8,9]
named_data = [111,121,131,141,51,36,4375,84356]

addition(a)
addition(named_data)

v = addition(a) + addition(named_data)

print(v)

# return
# is used to give the output from a fuction.
# will return the exact datatype.
# for a function there should be only one return.


def  addition(data):                
    b = 0
    for i in data:
        b = b + i
    print('above return will  be printed')
    
    return 10
    print('below return will not be printed')
    return b
a = [1,2,3,4,5,6,7,8,9]
named_data = [111,121,131,141,51,36,4375,84356]

b = addition(a) + addition(named_data)


print(b) # 20


def  addition(data):                
    b = 0
    for i in data:
        print(i)
        b = b + i
    print('above return will  be printed')
    
    return 100
    print('below return will not be printed')
    return b
a = [1,2,3,4,5,6,7,8,9]
named_data = [111,121,131,141,51,36,4375,84356]

b = addition(a) + addition(named_data)


print(b) # 200


def sample_fun(a,b):
    if a > b:
        print(a)
    else:
        return b

a = sample_fun(10,15)

print(a)

a = sample_fun(104,15)

c = a + 10 # error

print(c)

# a,b

# if a > b - a
# if b > a - a*b

def greater(a,b):
    if a>b:
        return a
    return b*a

c=greater(2,5)
print(c) # 10
c=greater(12,5)
print(c) # 12


def greater(a,b):
    if a>b:
        return [1,2,3,4,5]
    return ['1','2','3','4','5']

c=greater(2,5)
print(c) # ['1','2','3','4','5']0
c=greater(12,5)
print(c) # [1,2,3,4,5]

def greater_funciton_check(a,b):
    if a>b:
        return (1,2,3,4,5)
    return ['1','2','3','4','5']

c=greater_funciton_check(2,5)
print(c) # ['1','2','3','4','5']
c=greater_funciton_check(12,5)
print(c) # (1,2,3,4,5)

greater_fun = greater_funciton_check

print(greater_fun(2,5)) # ['1','2','3','4','5']


# lambda:
# 1. is used to create a simple single line function
# 2. by default lambda will return a output.
# 3. directly we cannoct call lambda
# 4. lambda will be given to a varibale and we will call that variable.

# syntax:
# lambda()


lambda a,b : a + b

lam = lambda a,b : a + b

print(lam(1,2)) # 3

lam = lambda a : int(a)

print(type(lam('1234'))) # 3
print((lam('1234'))) # 3


# agenda
# MRF
# comphrension

# Map | Filter | Reduce

# map:

# syntax:
# map(function,iterable_datatype)


# 1. output of the map is an iterator - list(),tuple(),set()
# 2. it will apply th elements in iterable_datatype to the functions one by one  
    # that function result will be stored in map iterator.
# 3. only one arguments should be used in functions


# map(funciton,a) # we should declare a function

a = [1,2,3,4,5]

def basic(n):
    return n * 10

b = list(map(basic,a))

c = list(map(lambda n : n*10 , a))
print(c)
print(b)

# a = input() # 1 3 5 7 9
# [5,15,25,35,45]