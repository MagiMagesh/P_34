
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
