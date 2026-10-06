from classimplementation import Car


class Driver:
    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no
        self.cars = []                      

    def add_car(self, car):
        self.cars.append(car)               

    def drive_all(self, distance):
        for car in self.cars:
            car.drive(distance)


if __name__ == "__main__":
    driver = Driver("Mr. Reyes", "N01-23-456789")
    car1 = Car("Toyota", "Vios", 2020, 30.0)
    car2 = Car("Honda", "Civic", 2022, 45.0)
    car3 = Car("Ford", "Ranger", 2019, 20.0)

    print("--- BEFORE RELATIONSHIP ---")
    print(f"{driver.name} owns {len(driver.cars)} car(s)")
    for c in (car1, car2, car3):
        print(" ", c)

    print("\n--- BUILDING RELATIONSHIP ---")
    for c in (car1, car2, car3):
        driver.add_car(c)
        print(f"Added {c.model} to {driver.name}")

    print("\n--- AFTER RELATIONSHIP ---")
    print(f"{driver.name} owns {len(driver.cars)} car(s):")
    for car in driver.cars:
        print(f"  {car.year} {car.make} {car.model} (fuel {car.get_fuel_level():.1f} L)")
    print("\nDriving all cars 100 km through the driver...")
    driver.drive_all(100)
    print("Original object car3 sees the change too:", car3)
    print("Same object?", driver.cars[2] is car3)
