from math import inf

res_ = 0

def divide(first, second):
    global res_
    first = int(first)
    second = int(second)
    if second == 0:
        return inf
    else:
        res_ = first / second

    return res_


# result= divide(50,0)
# print(result)