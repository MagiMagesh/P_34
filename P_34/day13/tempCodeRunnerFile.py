
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

print(a1.__dict__)
print(dir(a1))