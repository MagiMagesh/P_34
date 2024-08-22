def sample_fun(a,b):
    if a > b:
        print(a)
    else:
        return b

a = sample_fun(10,15)

print(a)

a = sample_fun(104,15)

c = a + 10 # error

print(c)