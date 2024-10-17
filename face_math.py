res_ = 0



def divide(first, second):
    global res_
    first = int(first)
    second = int(second)
    if second == 0:
       return ('Ошибка')
    else:
        res_ = first / second
    return res_


# result= divide(69,0)
# print(result)