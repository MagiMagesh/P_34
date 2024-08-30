'Counter',
'OrderedDict',
'deque',
'namedtuple',
'UserDict',
'UserList',
'UserString',


a = 'i live in India'
from collections import Counter
v = Counter(a)
print(type(v)) # similar to dict
print(v['i'])  
print(v)


from collections import Counter

a = [1,2,5,2,2,3,5,4,3,3,43,4,5,6,56,4,3,2,3,41,1,1,1,1,1]
print(Counter(a)) # {1:3,2:3}

# API - 

from collections import Counter,OrderedDict

d = {'key':'value','key2':'value2','key3':'value3',1:'value',2.1:'value2',('key3'):'value3'}
print(d.items())
d['magesh'] = 'Developer'
d['key'] = 'Developer'
print(d)


from collections import Counter,OrderedDict

b = OrderedDict([('key', 'value'), ('key2', 'value2'), ('key3', 'value3'), (1, 'value'), (2.1, 'value2')]) # [(k1,v1),(k2,v2),...]

print(b)

from collections import Counter,OrderedDict,namedtuple

a = namedtuple('x',['a','b','c'])

x_graph = a(10,15,20)

print(x_graph)



from collections import Counter,OrderedDict,namedtuple

a = namedtuple('RGB',['R','G','B'])

color = a(220,125,200)

print(color)



from collections import Counter,OrderedDict,namedtuple

a = namedtuple('Flowers',['Rose','Jasmine','Lotus','Sunflower'])

color = a("Red","Yellow","Pink",'Orange')

print(color)
color1 = a("Yello","White","White",'Red')

print(color1)


from collections import deque
# deque - it will also create list
#  popleft & appendleft

a = [1,2,3,4,5,"Red","Yellow",6,7,8,'Rose','Jasmine']
b = deque(a)
print(b)
b.popleft() # 1
b.popleft() # 2
print(b)
# print(dir(deque))


from collections import deque
# deque - it will also create list
#  popleft & appendleft

a = [1,2,3,4,5,"Red","Yellow",6,7,8,'Rose','Jasmine']
b = deque(a)
b.appendleft('Magesh')
print(b)


'UserDict',
'UserList',
'UserString',


from collections import UserString
# used in inheritance to create custom function for thiat string

class custom_str(UserString):

    def magesh(self):
        print('This is my function')

    # def 

a = 'Magesh'
# print(dir(str))

a1 = custom_str('Magesh it is my custom string')
print(a1)
a1.magesh()
# print(dir(a1))


a = 'i live in india my number is 234345876 my cost of this is 1200'
for i in a:
    try:
        if int(i) in range(10):
            print(i)
    except:
        pass

a = 'i live in india my number is 234345876 my cost of this is 1200'
for i in a:
    if i in list(map(str,range(10))):
        print(i)
    

a = 'i live in india my number is 234345876 my cost of this is 1200'
for i in a:
    if i.isdigit():
        print(i)



from collections import UserString

class custom_str(UserString):

    def magesh(self):
        print('This is my function')

    def to_take_numbers(self):
        new_str = ''
        for i in self:
            if i.isdigit():
                new_str = new_str + i
        return new_str

a1 = custom_str('i live in india my number is 234345876 my cost of this is 1200')

print(a1.to_take_numbers())


from collections import UserList

class custom_list(UserList):
# used in inheritance to create a custom function for that list


    def magesh(self):
        print('This is my function')

    def custom_print(self):
        for i in self:
            print(i)

a1 = custom_list([1,2,3,23,4,23,53,45,34,5,2,34,234,345])
a1.custom_print()

# unpacking operator - *
a = [1,2,3,23,4,23,53,45,34,5,2,34,234,345]
print(*a)

try:
    print(int('asd'))
except:
    print('there was an error')

try:
    a = 'Magsh'
    if a != 'Magesh':
        raise('There is an Error Occured')
    print(str('asd'))
except:
    print('there was an error')

try:
    a = 'Magsh'
    if a != 'Magesh':
        raise('There is an Error in Input')
    print(str('asd'))
except Exception as e: # 
    print('the error is: ',e)
    print('there was an error')


try:
    a = 'Magsh'
    int(a)
    print(str('asd'))
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')


try:
    a = 'Magsh'
    a + 10
    print(str('asd'))
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')

try:
    a = 'Magsh'
    10 / 0 #  10
    print(str('asd'))
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')



try:
    a = 'Magsh'
    10 / 0 #  10
    print(str('asd'))
except ZeroDivisionError:
    print('You are dividing with 0')
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')

# only the first occured except will be triggred
# we can have a multiple except block for a try block 

try:
    a = 'Magsh'
    10 / 0 #  10
    print(str('asd'))
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')
except ZeroDivisionError:
    print('You are dividing with 0')

try:
    a = 'Magsh'
    10 / 0 #  10
    print(str('asd'))
except IndexError:
    print('reduce the value and try')
except ZeroDivisionError:
    print('You are dividing with 0')
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')


try:
    a = 'Magsh'
    print(a[7])
    print(str('asd'))
except IndexError:
    print(f'try withing 0 to {len(a)-1}')
except ZeroDivisionError:
    print('You are dividing with 0')
except ValueError:
    print('thre is value error')
except TypeError:
    print('thre is type error')
except: # 
    print('there was an error')

a = [1,2,'3',4,5,[1,2,3,4,5],'12','34',12,3,['magesh','value']]
# 1,2,3,4,5,'magesh','value'

# have to use nested for loop
# 1. create empty list
# 2. to iterate to all the elements
# 3. to check the type wether it is list or not
# 4. if it is a list iterate that list
# 5. append the step4 element to the empty list