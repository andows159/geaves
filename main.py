


class DataInput():
    def __init__(self, amount_chicken,sell_price,buy_price,remedy,cleaning,price_before_initial,
    price_initial, price_growth, price_fattening, price_fuel, mortality, energy, water, 
    slaughter,autonomy):
        self.kg_all_days = [5,6,7.5,8.5,10,11,12.5,13.5,15,16,17.5,18.5,20,21,22.5,24,25.5,26,27.5,28,28.5,29.5,
        31.5,34,36,38,39,40,40.5,41.5,42.5,44,46,48,50,52,54,56.5,59,60.25,60.5,62.5,64,65,65,65,65,65,65,
        65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,
        65,65,65,65,65,65,65,65]
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
        #the method super doing class father to be activate 
        super().__init__(50,35,3.5,40,50,2.2,2.2,2.1,2.1,4.89,0.5,0,30,90,40)
        self.kg_before_initial(self.kg_all_days)

    def convert_gram_to_kilo(self,gram):
        return (gram /1000) * 2 
        #in addition to converting the unit, 
        # I multiply it by two, because the ration 
        # is placed twice a day, so the total is 
        # this multiplication

    def kg_before_initial(self, kg_all_days):
        before_initial = kg_all_days[0:15]
        sum_before_initial = 0
        for day in before_initial:
            sum_initial += day
        return self.convert_gram_to_kilo(sum_before_initial * self.amount_chicken)

    def kg_initial(self, kg_all_days):
        initial = kg_all_days[16:30]
        sum_initial = 0
        for day in initial:
            sum_initial += day
        return self.convert_gram_to_kilo(sum_initial * self.amount_chicken)


Status = Status()