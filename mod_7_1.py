from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category =category

    def __str__(self):
        return (f' {self.name}, {self.weight}, {self.category}')

class Shop:
    __file_name = 'product.txt'

    def get_product(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self,*product):
        file_get = self.get_product()
        for i in product:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продутк {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
print()
s1.add(p1,p2,p3)

print(s1.get_product())


