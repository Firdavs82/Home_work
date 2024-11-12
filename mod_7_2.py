def custom_write(file_name, strings):
    a = 0
    elem = {}
    for i in info:
        file = open(file_name, 'a',  encoding='utf-8' )
        tell = (file.tell())
        a += 1
        file.write(f'{i}\n')
        file.close()
        elem.update({(a, tell) : i })
    return elem


info = [
    'Text for tell.',
    'Использовать кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)