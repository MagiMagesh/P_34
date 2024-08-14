
# Q1. a = [1,2,'3',4,5,6,'7'] # add 5 to all these numbers

a = [1,2,'3',4,5,6,'7']

for i in a:
    print(int(i) + 5)

# Q2. a = [['Magesh','Good','1,2',345,345.456],3,4,5,['33,234,','one']]
    # need to get oo as otuput
    # need to get 345.456 as otuput

a = [['Magesh','Good','1,2',345,345.456],3,4,5,['33,234,','one']]
print(a[0])
print(a[0][1][1:3])
print(a[0][-1])

a = [[['Magesh','Good','1,2',345,345.456]],3,4,5,['33,234,','one']]
print(a[0])
print(a[0][0][1][1:3])