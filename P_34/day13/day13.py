
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


print(addition(aa1,ab1))
print(subract(aa1,ab1))
print(division(aa1,ab1))
print(power(ac1,ad1))
print(floor_div(ab1,ad1))

print(10*'-')


print(addition(aa2,ab2))
print(subract(aa2,ab2))
print(division(aa2,ab2))
print(power(ac2,ad2))
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