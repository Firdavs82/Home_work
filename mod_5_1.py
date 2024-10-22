class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        #self.go_to()


    def go_to(self,new_floor=1):
        new_floor = int(new_floor + 1)
        if new_floor < 1 or new_floor > (self.number_of_floors + 1):
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor):
                print(i)

            return new_floor





h1 = House('ЖК Городской', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# print(h1.name,h1.number_of_flors)
