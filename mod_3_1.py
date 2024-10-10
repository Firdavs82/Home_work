from collections import defaultdict
from itertools import count
from os import remove

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = (len(stroka),stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains (string,list_to_search):
    a = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == a:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('armagedon'))
print(is_contains('Urban',['ban','BaNan','urBAN']))
print(is_contains('cycle',['recycling','cyclic']))
print(calls)
