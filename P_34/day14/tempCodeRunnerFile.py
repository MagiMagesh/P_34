
def cricket():
    print('cricket')

def hockey():
    print('hockey')

def chess():
    print('chess')

def student_info(n,sport):
    print(n)
    print(sport())


n = int(input())
if n in range(15):
    if n == 5:
        student_info(n,hockey)
    elif n == 6 or n == 7:
        student_info(n,cricket)
    elif n == 3:
        student_info(n,chess)
    else:
        print('student should be enrolled in chess')
        student_info(n,chess)

