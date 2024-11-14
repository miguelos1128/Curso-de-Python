class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo {self.brand} {self.model}. ha sido vendido.')
        else:
            print(f'El vehiculo {self.brand} {self.model}. No esta disponible.')

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engines(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase") 

    def stop_engines(self):
         raise NotImplementedError("Este metodo debe ser implementado por la subclase") 
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"

    def stop_engines(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"
    
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_avalible:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
    def stop_engines(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicilceta {self.brand} no esta disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"

    def stop_engines(self):
        if self.is_available:
            return f"El motor del Camión {self.brand} se ha detenido"
        else:
            return f"El Camión {self.brand} no esta disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"El vehiculo {vehicle.brand} {vehicle.model} no esta disponible.")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
            print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} {vehicle.model} ha sido agregado al inventario.")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El {customer.name} ha sido añadido")

    def show_avalibe_vehicle(self):
        print("Vehiculos dsiponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

#Mostrar Vehiculos disponibles
dealership.show_avalibe_vehicle()

#Cliente consultar un Vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un Vehiculo
customer1.buy_vehicle(car1)

#Mostrar Vehiculos disponibles
dealership.show_avalibe_vehicle()



