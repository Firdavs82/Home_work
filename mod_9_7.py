def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        prime = True
        for i in range(2, res -1):
            if res % i == 0:
                prime = False
            if prime:
                print("Простое")
            else:
                print('Составное')
            return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    res_ = a + b + c
    return res_

result = sum_three(2, 3, 6)
print(result)
