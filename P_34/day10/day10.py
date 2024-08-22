# lambda:
# 1. is used to create a simple single line function

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

