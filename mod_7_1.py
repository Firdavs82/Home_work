from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category =category

    def __str__(self):
        return (f' {self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self, __file_name = 'product.txt'):
        super().__init__()
        self.__file_name = __file_name

    def get_product(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        # print(f' {self.__file_name}')

    def add(self,*product):
        self.get_product()
        file = open(self.__file_name, 'w')
        f = file.write(str(product))
        file.close()
        for i in product:
           if i in product:
                print(f'Продукт {i} уже есть в магазине')
                #file.close()
           else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{i}')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
print()
s1.add(p1,p2,p3)

print(s1.get_product())


