


class DataIput():

    def chicken_amount(self,amount):
        self.chicken = amount
        return self.chicken


DataIput = DataIput()

DataIput.chicken_amount(50)

print(type(DataIput.chicken_amount(50)))