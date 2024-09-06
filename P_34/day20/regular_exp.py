import re

# 1. findall    - output will be a list
# 2. search     - to tell wethere that pattern exists it will give first occured recored
# 3. match      - from starting till wherever it matches if everything matches then only we will be getting the result   
# 4. split

# re.findall(pattern,str)

# web scrapping| 

# keyword character
# /d - it is a number 0-9
# /w - it is a number a-z-A-z-0-9_
# /s - white space
# /D - opposite of /d
# /W - opposite of /w
# /S - opposite of /s
# /b
# /B
# /z
# /Z

# special character
# + - continuous matching of keyword characters
# []
# . - replace any one single character
# *
# {e} , {s,e}
# ^ - start
# $ - 

import re
a = 'my phone number is 123 234 my age is 12 door no is 3/'
pattern = '\d'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\w'
b = re.findall(pattern,a) 
print(b)

import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\s'
b = re.findall(pattern,a)  # [' ',' ',...]
print(b)

import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\D'
b = re.findall(pattern,a)  # [' ',' ',...]
print(b)

import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\W'
b = re.findall(pattern,a)  # [' ',' ',...]
print(b)


import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\S'
b = re.findall(pattern,a)  # [' ',' ',...]
print(b)

import re
a = 'my phone number is 123 234 my age is 12 door no is 3/'
pattern = '\d+'
b = re.findall(pattern,a) # ['123','234','12','3']
print(b)

import re
a = 'my phone number is 123 234 my age numberwer is 12 door no is 3/'
pattern = r'\bnumb'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = 'my phone number is 123 234 my age numberwer is 12 door no is 3/'
pattern = r'ber\b'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = 'my phone number is 123 234 my age numberwer is 12 door no is 3/'
pattern = r'ber\B'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

print('hi\nhello')
print(r'hi\nhello')

import re
a = 'my phone number is 123 234 my age is 12 door no is 3/'
pattern = '[a-zA-Z]'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = 'my phone number is asdf123lkjh 234 my age is 12 door no is 3/'
pattern = '[a-zA-Z]+'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = 'my phone number numzer is asdf123lkjh 234 my age is 12 door no is 3/'
pattern = 'num.er'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = 'my phone numbuerer numzrer num is asdf123lkjh 234 my age is 12 door no is 3/'
pattern = 'num*[a-z]+'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = '12323423 234234234234234234 98437782636 9843778263'
pattern = '\d{10}'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = '123423 1234423 12344231234423'
pattern = '\d{7,10}'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)

import re
a = '123423 1234423 12344231234423'
pattern = '^my'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = 'my pen mysore myinasd'
pattern = '^my'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = 'my pen mysore myinasd'
pattern = 'asd$'
b = re.findall(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)


import re
a = 'MY phone number is 123 234 my AGE is 12 door no is 3/'
pattern = '\w'
b = re.search(pattern,a) 
print(b)

import re
a = '123423 1234423 12344231234423'
pattern = '\d{7,10}'
b = re.search(pattern,a) # ['1','2','3','2',3','4','1','2','3']
print(b)
print(b.span())
print(b.group())


import re
a = '123423 1234423 12344231234423'
pattern = '\d{7,10}'
b = re.match(pattern,a) # ''
print(b)
if b:
    print('it is valid')

import re
a = '213.23_er-we4.234@asdf.asdf'
pattern = '[a-zA-Z0-9\.\_\-]+@[a-z]+\.[a-z]{3,4}'
b = re.match(pattern,a) # ''
print(b)
if b:
    print('it is valid')


import re
a = '213.23_er-we4.234@asdf.asdfda'
pattern = '[a-zA-Z0-9\.\_\-]+@[a-z]+\.[a-z]{3,4}$'
b = re.match(pattern,a) # ''
print(b)
if b:
    print('it is valid')