a = 293
for i in range(2,a):
    if a % i == 0:
        print('It is Not aPrime')
        break
else:
    print('It is Prime')