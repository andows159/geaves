from PyQt5 import uic, QtWidgets

class DataInput():
    def __init__(self, amount_chicken,sell_price,buy_price,remedy,cleaning,price_kg_before_initial,
    price_kg_initial, price_kg_growth, price_kg_fattening, price_fuel, mortality, energy, water, 
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
        self.price_kg_before_initial = price_kg_before_initial
        self.price_kg_initial = price_kg_initial
        self.price_kg_growth = price_kg_growth
        self.price_kg_fattening = price_kg_fattening
        self.price_fuel = price_fuel
        self.mortality = mortality
        self.energy = energy
        self.water = water
        self.slaughter = slaughter
        self.autonomy = autonomy
        #lembrar de chamar a janela de status apartir dessa classe 

class Status(DataInput):
    def __init__(self):
        #the method super doing class father to be activate 
        super().__init__(100,35,3.5,40,50,2.2,2.2,2.1,2.1,4.89,5,0,30,90,40)
        print(self.price_baby_chicken())
        print(self.value_brute())
        print(self.amount_food_kg())
        print(self.amount_food_price())
        print(self.amount_investiment())
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
            sum_before_initial += day
        return self.convert_gram_to_kilo(sum_before_initial * self.amount_chicken)

    def kg_initial(self, kg_all_days):
        initial = kg_all_days[15:30]
        sum_initial = 0
        for day in initial:
            sum_initial += day
        return self.convert_gram_to_kilo(sum_initial * self.amount_chicken)

    def kg_growth(self, kg_all_days):
        growth = kg_all_days[30:70]
        sum_growth = 0
        for day in growth:
            sum_growth += day
        return self.convert_gram_to_kilo(sum_growth * self.amount_chicken)

    def kg_fattening(self, kg_all_days):
        fattening = kg_all_days[70:90]
        sum_fattening = 0
        for day in fattening:
            sum_fattening += day
        return self.convert_gram_to_kilo(sum_fattening * self.amount_chicken)

    def price_before_initial(self):
        return self.price_kg_before_initial * self.kg_before_initial(self.kg_all_days)
    
    def price_initial(self):
        return self.price_kg_initial * self.kg_initial(self.kg_all_days)   
    
    def price_growth(self):
        return self.price_kg_growth * self.kg_growth(self.kg_all_days)
    
    def price_fattening(self):
        return self.price_kg_fattening * self.kg_fattening(self.kg_all_days)

    def price_baby_chicken(self):
        return self.amount_chicken * self.buy_price
    
    def value_brute(self):
        total = self.sell_price * self.amount_chicken
        percent = (self.mortality / 100) * total
        return total - percent

    def amount_food_kg(self):
        before_initial = self.kg_before_initial(self.kg_all_days)
        initial = self.kg_initial(self.kg_all_days)
        growth = self.kg_growth(self.kg_all_days)
        fattening = self.kg_fattening(self.kg_all_days)
        return before_initial + initial + growth + fattening

    def amount_food_price(self):
        return self.price_before_initial() + self.price_initial() + self.price_growth() + self.price_fattening()

    def amount_investiment(self):
        amount = self.amount_food_price() + self.price_fuel + self.energy + self.water + self.cleaning + self.remedy + self.slaughter
        return amount

class Screens(Status):
    def print_input(self):
        return print(self.screen_amount_chicken)

    def InputScreen(self):
        self.input_screen = uic.loadUi("./screens/input.ui")
        self.input_screen.show()
        self.screen_amount_chicken = self.input_screen.amount_chicken.text()
        self.screen_sell_price = self.input_screen.sell_price.text()
        self.screen_buy_price = self.input_screen.buy_price.text()
        self.screen_remedy = self.input_screen.remedy.text()
        self.screen_cleaning = self.input_screen.cleaning.text()
        self.screen_price_kg_before_initial = self.input_screen.price_kg_before_initial.text()
        self.screen_price_kg_initial = self.input_screen.price_kg_initial.text()
        self.screen_price_kg_growth =self.input_screen.price_kg_growth.text()
        self.screen_price_kg_fattening = self.input_screen.price_kg_fattening.text()
        self.screen_price_fuel = self.input_screen.price_fuel.text()
        self.screen_mortality = self.input_screen.mortality.text()
        self.screen_energy = self.input_screen.energy.text()
        self.screen_water = self.input_screen.water.text()
        self.screen_slaughter = self.input_screen.slaughter.text()
        self.screen_autonomy = self.input_screen.autonomy.text()
        
        

        self.input_screen.print_input.clicked.connect(self.print_input)

class Main(Screens):
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.InputScreen()
        app.exec()        




inst = Main()