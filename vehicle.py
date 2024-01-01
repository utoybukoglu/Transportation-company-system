class Vehicle:
    def __init__(self, VehicleID = -1, Brand = "Undefined", Model = "Undefined", PlateNo = "Undefined"):
        self.VehicleID = VehicleID
        self.Brand = Brand
        self.Model = Model
        self.PlateNo = PlateNo

    def getVehicleID(self):
        return self.VehicleID
    
    def getBrand(self):
        return self.Brand
    
    def getModel(self):
        return self.Model

    def getPlateNo(self):
        return self.plateNo
    
    def printVehicle(self):
        print(f"Vehicle ID: {self.VehicleID}, Brand: {self.Brand}, Model: {self.Model}, Plate No: {self.PlateNo}")
