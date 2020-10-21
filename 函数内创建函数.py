def outer():
    m = 100

    def inner():
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    #return inner


#inner()
# inner函数在外部不能直接调用
#outer()()
outer()