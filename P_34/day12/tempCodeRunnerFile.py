class school_class:

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    
    def student_name(self):
        print(f'it is Name function {self.name}')

    def student_sex(self):
        print('it is sex function',self.sex)

    def name_sex(self):
        print(f'Name is {self.name} and sex is {self.sex}')



s1 = school_class('Magesh','m')

s1.student_name()
s1.student_sex()
s1.name_sex()

