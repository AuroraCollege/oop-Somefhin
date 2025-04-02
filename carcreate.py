# create car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return(self.year, self.make, self.model)

one = Car('Toyota' , 'Camry' , 2009)
print(one.display_info())