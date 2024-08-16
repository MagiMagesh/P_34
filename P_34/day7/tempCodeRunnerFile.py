a = '112312312423423534545654'

b = ''
for i in a:
    if i not in b:
        b = b + i
print(b)