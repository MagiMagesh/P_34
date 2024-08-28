a = [1,2,3,4,5,6,7]

1
2
3
4
5
6
7
2
4
6
8

# yield
# class


a = [1,2,3,4,5,6,7]
for i in a:
    for j in a:
        print(i*j)
    print(10*'-')


# Function:
# two ways to return output
    # 1. return
        # there will be only one return for a function.
        # it gives output in only one datatype.
    # 2. yield
        # there will be many yield for a function.
        # yield inside a funciton will produce generator.
        # to take output from generator we need to uer keyword next
        # once if we take any data from generator it will not be present in generator

# should not use both 
# either Yield or return should be used based on the usecase

def check_function():
    print('Magesh')
    return 'Magesh',123


print(check_function())


def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function() # generator

a1 = next(v) # 'Magesh'
a2 = next(v) # 123

print(a1)
print(a2)

print(next(v)) # 123.123
print(next(v)) # '123.123'
print(next(v)) # Error


# generator is a iterable data-type:


def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

for i in v:
    print(i)

print(next(v)) # Error

def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

a1 = list(v)
print(a1) # ['Magesh',123,123.123,'123.123']

def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

a1 = set(v)
print(a1) # {'Magesh',123,123.123,'123.123'}

def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

a1 = tuple(v)
print(a1) # {'Magesh',123,123.123,'123.123'}


def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

a1 = list(v)
print(a1) # ['Magesh',123,123.123,'123.123']
print(next(v)) # error

def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

for i in v:
    pass
a1 = next(v)
print(a1) # Error


def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

for i in v:
    if i == 123:
        break
a1 = list(v)
print(a1) # [123.123 , '123.123']


def yield_function():
    yield 'Magesh'
    yield 123
    yield 123.123
    yield '123.123'


v = yield_function()

for i in v:
    if i == 123.123:
        break
a1 = list(v)
print(a1) # ['123.123']


def yield_function(a,b,c,d):

    if a > b:
        yield 10

    if c > a:
        yield 10

    if a > d:
        yield 15

    if c > d:
        yield 20
    
a = yield_function(10,15,231,43)
print(list(a))



# class:
# OOPS - Object Oriented Programming


a = [1,2,3,4,5]
a.append(5)

print(type([234])) # <class 'int'>
print(list('123'))


# car

# dashboard
# fuel injection
# front axle
# rear axle
# boot
# Engine


class car:
    pass


a = car()
b = car()

print(car())

class school_class:
    pass

first = school_class()
second = school_class()
thrid = school_class()


first.class_name =  'First Standard'
first.strength =  20
first.names =  ['Magesh',"Ram",'Shiva']

print(first.__dict__) # {'class_name':'First Standard',..}

# self instance of that Object. i.e Object represent class

class school_class:
    
    def name(self):
        print('it is Name function')

    def sex(self):
        print('it is sex function')

s1 = school_class()

s1.name()
s1.sex()



class school_class:

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    
    def student_name(self):
        print(f'it is Name function {self.name}')

    def student_sex(self):
        print('it is sex function',self.sex)

    def name_sex(self):
        print(f'Name is {self.name} and sex is {self.sex}')



s1 = school_class('Magesh','M')

s1.student_name()
s1.student_sex()
s1.name_sex()

# Q1. find wether a number is prime or not 56:

a = 292
prime = True
for i in range(2,a):
    if a % i == 0:
        print(i)
        prime = False
        break

if prime:
    print('It is a prime number')
else:
    print('It is not a prime number')



a = 293
for i in range(2,a):
    if a % i == 0:
        print('It is Not aPrime')
        break
else:
    print('It is Prime')

# if for loops is not got terminated by default else will be triggred


# Q2. 1234 to print all the prime number in that range
