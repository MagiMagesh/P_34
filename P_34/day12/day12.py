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
# inheritance
# method overriding

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
