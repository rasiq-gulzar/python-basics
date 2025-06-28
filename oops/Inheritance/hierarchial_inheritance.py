# syntax :
#     class parent:
#         pass
#     class childclass(parent):
#         pass
#     class childclass2(parent):
#         pass

class Vehicle:
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed
        
    def displayf(self):
        print(f'Brand {self.brand}')
        print(f'Color {self.color}')
        print(f'Speed {self.speed}')
        
class Car(Vehicle):
    def __init__(self,brand,color,speed,model):
         super().__init__(brand,color,speed)
         self.model=model
        
    def car_details(self):
        print(f'Model {self.model}')
        
class Bike(Vehicle):
    def __init__(self,brand,color,speed,type_of_byke):
         Vehicle.__init__(self,brand,color,speed)
         self.type_of_byke=type_of_byke
         
    def bike_details(self):
        print(f'Type of the bike is {self.type_of_byke}')

#multilevel inheritance
class SupBike(Bike):
    def __init__(self,brand,color,speed,type_of_byke,turboEngine):
        Bike.__init__(self,brand,color,speed,type_of_byke)
        self.turboEngine=turboEngine
        
    def turbo_engine(self):
        print(f'Turbo Engine is {self.turboEngine}')


#multiple inheritance
class ElonMusk(SupBike,Car):
    def __init__(self,brand,color,speed,type_of_byke,turboEngine,model,owns):
        SupBike.__init__(self,brand,color,speed,type_of_byke,turboEngine)
        Car.__init__(self,brand,color,speed,model)
        self.owns=owns
    def musk_owns(self):
        print(f'Elon Musk owns {self.owns}')
               
supbike=SupBike('Yamaha','Blue',200,'Racing','Dual Turbo Nitro Engine')

print('Multi level Inheritance: ')
supbike.displayf()
supbike.bike_details()
supbike.turbo_engine()

print('mulitple level inheritance: ')
elon=ElonMusk('Tesla','Black',250,'model x','racing','Dual Turbo Nitro Engine','all these companies and brands')
elon.displayf()
elon.car_details()
elon.turbo_engine()
elon.musk_owns()
