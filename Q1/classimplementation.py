class Car:
    def __init__(self, make, model, year, fuel_level, mileage = 0.0):
        self.make = make                   
        self.model = model                
        self.year = year                    
        self.__fuel_level = fuel_level     
        self.__mileage = mileage            
        self.__tank_capacity = 50.0         
 
    def drive(self, distance):
        needed = distance / 10
        if distance <= 0:
            print("Distance must be positive.")
        elif needed > self.__fuel_level:
            print(f"{self.model}: not enough fuel to drive {distance} km.")
        else:
            self.__fuel_level -= needed
            self.__mileage += distance
 
    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return
        self.__fuel_level = min(self.__fuel_level + amount, self.__tank_capacity)
 
    def get_fuel_level(self):
        return self.__fuel_level
 
    def get_mileage(self):
        return self.__mileage
 
    def honk(self):
        print(f"{self.model} says: Beep beep!")
 
    def __str__(self):
        return (f"{self.year} {self.make} {self.model} | "
                f"fuel={self.__fuel_level:.1f} L | mileage={self.__mileage:.1f} km")
 if __name__ == "__main__":
    car1 = Car("Toyota", "Vios", 2020, 30.0)
    car2 = Car("Honda", "Civic", 2022, 45.0)
 
    print("--- BEFORE ---")
    print("Object 1:", car1)
    print("Object 2:", car2)
    print("\nPerforming car1.drive(120)...\n")
    car1.drive(120)
    print("--- AFTER ---")
    print("Object 1:", car1)
    print("Object 2:", car2)
