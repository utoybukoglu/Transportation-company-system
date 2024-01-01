from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, VehicleID=-1, Brand="Undefined", Model="Undefined", PlateNo="Undefined", carTpye = None):
        super().__init__(VehicleID, Brand, Model, PlateNo)
        self.carType = carTpye
        self.seatNum = None

        if self.carType == "Sedan" or self.carType == "Hatchback":
            self.seatNum = 5
        elif self.carType == "Limousine":
            self.seatNum = 6
        else:
            raise Exception("Enter a valid car type!")
        
    def getSeats(self):
        return self.seatNum
    
    def checkSuitability(self, NumberOfPeople):
        if self.seatNum >= NumberOfPeople:
            return True
        else:
            return False

    def annualCost(self, KM):
        return KM * 10

    def printVehicle(self):
        super().printVehicle()
        print(f"Car Type: {self.carType}")

    def getObjectType(self):
        return "Car"