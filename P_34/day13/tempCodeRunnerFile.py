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