
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
        return  self.a + self.b


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

print(a1.addition())
print(a1.subract())
print(a1.division())
print(a1.power())
print(a1.floor_div())

print(10*'-')

a2 = arithmetic(25,10,200,2)

print(a2.addition())
print(a2.subract())
print(a2.division())
print(a2.power())
print(a2.floor_div())