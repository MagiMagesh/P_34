
a = 10
b = 20

class arithmetic:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def addition(self):
        print('it is addition funtion')
        # return  a + b # a & b will be treated as global variable
        return  self.a + self.b + a


    def subract(self):
        print('it is subract funtion')
        return  self.a - self.b

    def division(self):
        print('it is division funtion')
        return  self.a / self.b
    
    def power(self):
        print('it is power funtion')
        return  self.c ** self.d
    
    def floor_div(self):
        print('it is floor div funtion')
        return  self.b // self.d



a1 = arithmetic(15,30,20,3)

print(a1.__dict__) # attribute assigned to this class
print(dir(a1))

a2 = arithmetic(25,10,200,2)

print(a1.addition()) # 45
print(a2.division()) # 2.5
print(a2.power()) # 40000 
print(a1.power()) # 8000 
print(a1.floor_div()) # 10

print(10*'-')


print(a2.addition()) # 35
print(a2.subract()) # 15
print(a1.subract()) # -15
print(a1.division()) # 0.5
print(a2.floor_div()) # 5



def addition(a,b):
    print('it is addition funtion')
    return  a + b


def subract(a,b):
    print('it is subract funtion')
    return  a - b

def division(a,b):
    print('it is division funtion')
    return  a / b

def power(c,d):
    print('it is power funtion')
    return  c ** d

def floor_div(b,d):
    print('it is floor div funtion')
    return  b // d

aa1 = 15
ab1 = 30
ac1 = 20
ad1 = 3

aa2 = 25
ab2 = 10
ac2 = 200
ad2 = 2


print(subract(aa1,ab1))
print(division(aa2,ab2))
print(power(ac2,ad2))
print(division(aa1,ab1))
print(floor_div(ab1,ad1))

print(10*'-')


print(addition(aa2,ab2))
print(subract(aa2,ab2))
print(power(ac1,ad1))
print(addition(aa1,ab1))
print(floor_div(ab2,ad2))




class arithmetic:

    def __init__(self,a,b):
        self.area = a # for our understanding we ill be using the input argument itself
        self.b = b
        

    def addition(self):
        print('it is addition funtion')
        return  self.area + self.b
    
    def division(self):
        print('it is div funtion')
        return  self.m / self.n
    
    def multi(self):
        print('it is multi funtion')
        return  self.m * self.n
    
a1 = arithmetic(10,20)

print(a1.multi()) # since thre is no m & n is assigned so we will get an error


a1.m = 15
a1.n =  2

print(a1.__dict__)


print(a1.division())




class arithmetic:

    def __init__(self,a,b):
        self.area = a # for our understanding we ill be using the input argument itself
        self.b = b
        

    def addition(self):
        print('it is addition funtion')
        return  self.area + self.b
    
    def division(self):
        print('it is div funtion')
        return  self.m / self.n
    
    def multi(self,z):
        print('it is multi funtion')
        return  self.m * self.n * z
    
a1 = arithmetic(10,20)


a1.m = 15
a1.n =  2


print(a1.multi(10)) # 2000


name = 'Magesh'

class arithmetic:

    # name = name # class arguments are static / global variable
    name =  'Magesh' # class arguments are static / global variable
    age = 20

    def __init__(self,a,b):
        self.area = a # for our understanding we ill be using the input argument itself
        self.b = b
        

    def addition(self):
        print('it is addition funtion')
        return  self.area + self.b
    
    @staticmethod
    def non_relational_function(self):
        print('it is not relaed to class')
        print('it is a satic method')
        print(self) # 10

    @classmethod
    def class_function(cls):
        print('it is not relaed to class')
        print('it is a satic method')
        print(cls.name) 
        print(cls.age) 

a1 = arithmetic(10,20)

a1.non_relational_function(10)
a1.class_function()





class arithmetic:

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def addition(self):
        print('it is addition funtion')
        print(f'the combined result of subract & div {self.subract() * self.div()}')
        return  self.a + self.b 


    def subract(self):
        print('it is subract funtion')
        return  self.a - self.b
    
    def div(self):
        print('it is subract funtion')
        return  self.a / self.b
    
    def combined(self):

        return self.subract() * self.addition()
    
a1 = arithmetic(15,30)


print(a1.addition()) # 45
print(a1.subract()) # 45
print(a1.combined()) # 45


class pricipal:

    def __init__(self,name,salary,age):
        self.salary = salary
        self.age = age
        self.name = name


    def salary_check(self):
        print(f'salary is {self.salary}')
    
    def increment(self,percentage):
        self.salary = self.salary * (1+(percentage/100))

    
        

p1 = pricipal('Magesh',100000,20)
p1.salary_check()
print(p1.__dict__)
p1.increment(20)
print(p1.__dict__)
p1.increment(15)
print(p1.__dict__)


# ------------------------------------------------    INHERITANCE ----------------------------------------------------

class parent:

    def assets(self):
        return 2_00_00_000
    
    def addition(self):
        return 20

    def sub(self):
        return 10

class child(parent): # inheritance child is inheriting all the mehtods and attribute of parent class

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def child_info(self):
        print('cihld info')
        assets = self.assets()
        print(self.name ,self.age ,self.sex,assets)

c1 = child('Magesh',20,'M')
print(dir(c1))
c1.child_info()
print(c1.assets())
print(c1.addition())
print(c1.sub())




class parent:

    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def assets(self):
        return 2_00_00_000
    
    def addition(self):
        return 20

    def sub(self):
        return 10

class child(parent): # inheritance child is inheriting all the mehtods and attribute of parent class

    # def __init__(self, name,age,sex,father_name, mother_name):
    #     super().__init__(father_name, mother_name)

    
    # def __init__(self, name,age,sex,*args): # input should be like this ('Magesh',20,'M','Earth','Moon')
    #     super().__init__(*args)

    def __init__(self, name,age,sex,**kwargs): # input should be like this ('Magesh',20,'M','Earth','Moon')
        super().__init__(**kwargs)
        
        self.name = name
        self.age = age
        self.sex = sex

    def child_info(self):
        print('cihld info')
        assets = self.assets()
        print(self.name ,self.age ,self.sex,assets)

    def parent_details(self):
        print('father name is',self.father_name)
        print('mother name is',self.mother_name)

    

c1 = child(father_name='Ashok',mother_name='Saraswathi',name='Magesh',age=20,sex='M')
c1.parent_details()


class parent:
    def name(self):
        print('this is name')

class parent:
    def name(self):
        print('this is name')

    def sum(self,a):
        b = 1
        for i in a:
            b = b * i
        return b


# def sum(a): # will replace python inbuilt funciton not recommended
#     b = 1
#     for i in a:
#         b = b * i
#     return b

a1 = parent()

a = [1,2,3,4,5] # 120
print(sum(a)) # 120
print(a1.sum(a))


# 1. inheritance
# 2. multiple inheritance
# 3. method overriding | 
