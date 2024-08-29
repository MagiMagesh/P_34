for a in range(2,2000+1):
    for i in range(2,a):
        if a % i == 0:
            prime = False
            break
    else:
        print(a,'it is prime number')