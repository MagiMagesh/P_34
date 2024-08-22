a = [1,2,3,4,5]

def basic(n):
    return n * 10

b = list(map(basic,a))

c = list(map(lambda n : n*10 , a))
print(c)
print(b)