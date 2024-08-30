try:
    a = 'Magsh'
    print(a[7])
    print(str('asd'))
except IndexError:
    print(f'try withing 0 to {len(a)-1}')
except ZeroDivisionError:
    print('You are dividing with 0')
except Exception as e: # 
    print('the error is: ',e)
    print('the type of error is: ',type(e))
    print('there was an error')