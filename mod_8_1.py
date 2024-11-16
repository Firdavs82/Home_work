def add_everythin_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int,float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError

    except TypeError:
        return f'{str (a)}{str (b)}'


print(add_everythin_up(123.456,'строка'))
print(add_everythin_up('яблоко', 4215))
print(add_everythin_up(123.456, 7.0))