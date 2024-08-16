a = [1,'123','magesh','234.234',345,'phone','11',234.234,'zer','Earth','Moon','Mars']

# print(a[1].isdigit()) # True
# print(a[2].isdigit()) # False

for i in a:
    if type(i) ==str:
        if i.isdigit():
            print(float(i)+5)
    if type(i) ==int:
        print(i + 5)
    if type(i) ==float:
        print(i + 5)
    