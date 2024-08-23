try:
    try:
        if 41 > 5:
            print(1)
        print(list('1234'))
        print(''* '')

        print(int('9876'))
    except:
        print(''* '')
        print('thre was error')
    finally:
        print('THere was an emergency')
except:
    print('there was new error')