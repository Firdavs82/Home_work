from math import trunc


def print_params(a = 1,b ='Строка',c = True):
    print(a, b, c)

print_params()
print_params(12, "hi",False)
print_params(3, 25 ,[1,2,3])
print()

values_list = ['hello',True,55]
values_dict = {"a":13,"b":'Привет',"c":[5,6,7]}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32 ,'Строка']
print_params(*values_list_2,42)
