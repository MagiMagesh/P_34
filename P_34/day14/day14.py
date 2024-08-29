from day14_2 import addition_values

print(addition_values([1,2,3,4]))

class parent:
    def name(self):
        print('this is name')

    def sum(self,a):
        b = 1
        for i in a:
            b = b * i
        return b
    
a1 = parent()
a = [1,2,3,4,5] # 120
print(sum(a)) # 120
print(a1.sum(a))



class dog:
    def sound(self):
        print('bark')

class snake(dog):
    def sound(self):
        print('hissing')

    


s1 = snake()
s1.sound()
d1 = dog()
d1.sound()


# higher order function:
# function as arguemnts

def like():
    return 'I like you'

def hate():
    return 'I hate you'

def user_name(name,any_function):
    print( name)
    print(any_function())

name = 'Kagesh'
if name == 'Magesh':
    user_name(name,like) # like function is assigned to any_function
else:
    user_name(name,hate) # hate function is assigned to any_function

print(3 in [1,2,3,4,5,6,7]) # True
print(3 in ['1','2','3','4','5','6','7']) # False
print(4 in range(5))


def cricket():
    print('cricket')

def hockey():
    print('hockey')

def chess():
    print('chess')

def student_info(n,sport):
    print(n)
    print(sport())


n = int(input())
if n in range(15):
    if n == 5:
        student_info(n,hockey)
    elif n == 6 or n == 7:
        student_info(n,cricket)
    elif n == 3:
        student_info(n,chess)
    else:
        print('student should be enrolled in chess')
        student_info(n,chess)



class dog:

    def getinput_dog(self):
        print('getinput_dog')

class cat:

    def getinput_cat(self):
        print('getinput_cat')

class snake(dog,cat):
    
    def __init__(self, c,d):
        self.c = c
        self.d = d

    def getinput_snake(self):
        print(self.c , self.d)

s1 = snake(10,20)
print(dir(s1))


class dog:

    def __init__(self,a,b):
        self.a = a

    def getinput_dog(self):
        print(self.a , self.b)

class cat:

    def __init__(self,e):
        self.e = e

    def getinput_cat(self):
        print(self.e , self.f)

class snake(dog,cat):
    
    def __init__(self, c,d,a,e):
        super().__init__(a)
        super(cat,self).__init__(e)
        
        self.c = c
        self.d = d


    def getinput_snake(self):
        print(self.c , self.d,self.a,self.e)

s1 = snake(1,2,3,4)
print(dir(s1))
s1.getinput_snake()

# LIFO  - Last in first out functions or class

def fun1():
    fun2()
    print(1)

def fun2():
    fun3()
    print(2)

def fun3():
    fun4()
    print(3)

def fun4():
    fun5()
    print(4)

def fun5():
    print(5)

fun1()


