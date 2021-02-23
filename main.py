


class DataInput():
    def __init__(self, amount_chicken,sell_price,buy_price,remedy,cleaning,price_before_initial,
    price_initial, price_growth, price_fattening, price_fuel, mortality, energy, water, 
    slaughter,autonomy):
        self.amount_chicken = amount_chicken
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.remedy = remedy
        self.cleaning = cleaning
        self.price_before_initial = price_before_initial
        self.price_initial = price_initial
        self.price_growth = price_growth
        self.price_fattening = price_fattening
        self.price_fuel = price_fuel
        self.mortality = mortality
        self.energy = energy
        self.water = water
        self.slaughter = slaughter
        self.autonomy = autonomy
        

#DataInput = DataInput(50,35,3.5,40,50,2.2,2.2,2.1,2.1,4.89,0.5,0,30,90,40)

class Status(DataInput):
    def __init__(self):
        super().__init__(50,35,3.5,40,50,2.2,2.2,2.1,2.1,4.89,0.5,0,30,90,40)
        print(self.autonomy)
        


 
 