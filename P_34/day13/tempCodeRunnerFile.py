

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