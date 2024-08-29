
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