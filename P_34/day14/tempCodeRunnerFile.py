def fun1():
    fun2()
    print(1)

def fun2():
    fun3()
    print(2)

def fun3():
    fun4()
    print(3)

def fun4():
    fun5()
    print(4)

def fun5():
    print(5)

fun1()