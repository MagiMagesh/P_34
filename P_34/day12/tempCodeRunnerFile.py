def yield_function(a,b,c,d):

    if a > b:
        yield 10

    if c > a:
        yield 10

    if a > d:
        yield 15

    if c > d:
        return 20
    
a = yield_function(10,15,23,43)
print(list(a))