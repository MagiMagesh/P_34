
n = int(input()) # 7
numbers = input().split() # '1 15 11 121 131 159 98'.split(' ')
print(numbers)

b = []
output = None
for i in range(len(numbers)):
    if numbers[i]  in b:
        output = i
    b.append(numbers[i])

if output:
    print(output)
    print(b)
else:
    print(-1)