# .isupper()
# .islower()
# .isalnum
# .isalpha
# .isdigit
# strip, rstrip, lstrip
# join
# .split


# .isupper() output will be in bool - wether all the alphabtes in that string is Uppercase
# .islower() output will be in bool - wether all the alphabtes in that string is LowerCase
# .isalnum() output will be in bool - wether all the element in that string is either alphabtes (A-Za-z0-9)
# .isalpha() output will be in bool - wether all the element in that string is alphabtes
# .isdigit() output will be in bool - wether all the element in that string is number

a = 'I live in India'
print(a.isalnum()) # False - space is not alphabets or number

a = 'India'
print(a.isalnum()) # True

a = 'It234is345abigs345enten345ce'
print(a.isalnum()) # True

a = 'It234is345abigs345enten345ce'
print(a.isalpha()) # False

a = '234324534534'
print(a.isalnum()) # True

a = '234324534534'
print(a.isdigit()) # True

a = '234324534534'
print(a.isdecimal()) # True

a = '2343245.34534'
print(a.isdecimal()) # False


a = 'HI THIS IS MAGESH'
print(a.isupper()) # True


a = 'HI TH2343IS IS 234234MAGESH'
print(a.isupper()) # True

a = 'HI TH2343iS IS 234234MAGESH'
print(a.isupper()) # False


a = 'i live in india'
print(a.islower()) # True