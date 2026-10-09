#Üst Sınıf
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f'{self.brand} - {self.model}')


class Suv(Vehicle):
    def __init__(self,brand,model,awd):
        super().__init__(self,brand,model)
        self.awd = awd

    def show_info(self):
        print(f'{self.brand} - {self.model} - awd')



arac_brand = input('Aracın Markasını Girin: ')
arac_model = input('Aracın Modelini Girin: ')
arac_awd = input('Araç SUV model mi? (e/h): ')

arac = Vehicle(arac_brand,arac_model)
arac.show_info()