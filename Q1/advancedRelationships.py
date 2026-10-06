class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders

    def describe(self):
        return f"{self.horsepower} hp, {self.cylinders}-cylinder"


class Vehicle:                              
    def __init__(self, make, model, year, plate_number):
        self.make = make
        self.model = model
        self.year = year
        self.plate_number = plate_number
        self._mileage = 0.0

    def get_mileage(self):
        return self._mileage

    def display_info(self):
        return f"{self.year} {self.make} {self.model} [{self.plate_number}]"


class Car(Vehicle):                          
    def __init__(self, make, model, year, plate_number,
                 fuel_level, horsepower, cylinders):
        super().__init__(make, model, year, plate_number)
        self.__fuel_level = fuel_level
        self.engine = Engine(horsepower, cylinders)   

    def drive(self, distance):
        needed = distance / 10
        if 0 < distance and needed <= self.__fuel_level:
            self.__fuel_level -= needed
            self._mileage += distance
        else:
            print(f"{self.model}: cannot drive {distance} km.")

    def refuel(self, amount):
        if amount > 0:
            self.__fuel_level = min(self.__fuel_level + amount, 50.0)

    def get_fuel_level(self):
        return self.__fuel_level


class Motorcycle(Vehicle):                   
    def __init__(self, make, model, year, plate_number, has_sidecar):
        super().__init__(make, model, year, plate_number)
        self.has_sidecar = has_sidecar

    def ride(self, distance):
        self._mileage += distance


class GasStation:
    def __init__(self, name):
        self.name = name

    def fill(self, car, amount):
        print(f"{self.name} fills {car.model} with {amount} L")
        car.refuel(amount)


class Driver:
    def __init__(self, name):
        self.name = name
        self.vehicles = []                   

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def refuel_at(self, station, car, amount):   
        station.fill(car, amount)


if __name__ == "__main__":
    car1 = Car("Toyota", "Vios", 2020, "ABC 123", 30.0, 106, 4)
    moto1 = Motorcycle("Honda", "Click", 2021, "XYZ 789", False)
    driver = Driver("Mr. Reyes")
    station = GasStation("Petron")

    print("=== TEST 1: INHERITANCE ===")
    print("Car plate_number (from Vehicle):", car1.plate_number)
    print("Car display_info (from Vehicle):", car1.display_info())
    print("Motorcycle display_info (from Vehicle):", moto1.display_info())
    car1.drive(100)
    moto1.ride(25)
    print("Car mileage:", car1.get_mileage(), "| Motorcycle mileage:", moto1.get_mileage())
    print("isinstance(car1, Vehicle):", isinstance(car1, Vehicle))

    print("\n=== TEST 2: COMPOSITION / AGGREGATION ===")
    print("Composition -> Car contains Engine:", car1.engine.describe())
    driver.add_vehicle(car1)
    driver.add_vehicle(moto1)
    print(f"Aggregation -> {driver.name} has vehicles:")
    for v in driver.vehicles:
        print("  -", v.display_info())
    del driver
    print("Driver deleted, car still exists:", car1.display_info())

    print("\n=== TEST 3: DEPENDENCY ===")
    driver2 = Driver("Ms. Santos")
    print("Fuel before:", car1.get_fuel_level())
    driver2.refuel_at(station, car1, 15)
    print("Fuel after:", car1.get_fuel_level())
