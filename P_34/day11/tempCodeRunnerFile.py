a = [1,2,3,4,5,6,7]
k = 7
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i]+a[j])