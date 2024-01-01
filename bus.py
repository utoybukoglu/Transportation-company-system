from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, VehicleID=-1, Brand="Undefined", Model="Undefined", PlateNo="Undefined", NumberOfSeats = 0):
        super().__init__(VehicleID, Brand, Model, PlateNo)
        self.NumberOfSeats = NumberOfSeats

    def checkSuitability(self, NumberOfPeople):
        if self.NumberOfSeats >= NumberOfPeople:
            return True
        else:
            return False
    
    def annualCost(self, maintenanceCost, NumberOfTimesServiced):
        return maintenanceCost * NumberOfTimesServiced

    def printVehicle(self):
        super().printVehicle()
        print(f"Car Type: Bus, Number of Seats: {self.NumberOfSeats}")

    def getObjectType(self):
        return "Bus"