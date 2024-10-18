def test_function():
    hi_ = 'Helo function'
    print(hi_)
    def inner_function():
        nonlocal hi_
        hi_=('Я в области видимости функции',test_function)
        print(hi_)

    inner_function()
    return hi_

test_function()
#inner_function()