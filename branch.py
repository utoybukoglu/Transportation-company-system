from car import Car
from bus import Bus 

class Branch:
    def __init__(self, BranchID=-1, City="Undefined", NumberOfVehicles=0):
        self.BranchID = BranchID
        self.City = City
        self.Vehicles = []
        self.NumberOfVehicles = NumberOfVehicles

    def getBranchID(self):
        return self.BranchID

    def addVehicle(self):
        print("What kind of vehicle would You like to add?")
        print("Possible options: (0) Bus, (1) Sedan, (2) Hatchback, (3) Limousine")
        choice = int(input("Your choice: "))
        if choice < 0 or choice > 3:
            print("Enter a valid choice!")
        elif choice == 0:
            ID = int(input("Please enter the ID of the vehicle: "))
            brand = input("Please enter the brand of the vehicle: ")
            model = input("Please enter the model of the vehicle: ")
            plateNo = input("Please enter the plate number of the vehicle: ")
            seatNo = int(input("Please enter the number of seats on the Bus: "))
            tempBus = Bus(ID, brand, model, plateNo, seatNo)
            self.Vehicles.append(tempBus)
        else:
            ID = int(input("Please enter the ID of the vehicle: "))
            brand = input("Please enter the brand of the vehicle: ")
            model = input("Please enter the model of the vehicle: ")
            plateNo = input("Please enter the plate number of the vehicle: ")
            carType = None
            if choice == 1:
                carType = "Sedan"
            elif choice == 2:
                carType = "Hatchback"
            else:
                carType = "Limousine"
            tempCar = Car(ID, brand, model, plateNo, carType)
            self.Vehicles.append(tempCar)
        print("Vehicle is successfully added!")
        self.NumberOfVehicles += 1

    def printBranch(self):
        print(f"City: {self.City}, Number of vehicles: {self.NumberOfVehicles}")

    def printVehicles(self):
        for vehicle in self.Vehicles:
            vehicle.printVehicle()
            print()

    def printVehiclesByType(self, choice):
        if choice != 0 and choice != 1:
            raise Exception("Enter a valid choice!!")
        elif choice == 0:
            for vehicle in self.Vehicles:
                if vehicle.getObjectType() == "Bus":
                    print(f"Vehicles at Branch with ID {self.BranchID}:")
                    vehicle.printVehicle()
                    
        else:
            for vehicle in self.Vehicles:
                if vehicle.getObjectType() == "Car":
                    print(f"Vehicles at Branch with ID {self.BranchID}:")
                    vehicle.printVehicle()

    def printTypeStatistics(self):
        carNum = 0
        busNum = 0
        for vehicle in self.Vehicles:
                if vehicle.getObjectType() == "Car":
                    carNum += 1
                else:
                    busNum += 1
        print(f"At Branch with ID {self.BranchID} there are:")
        print(f"   {busNum} bus(es)")
        print(f"   {carNum} car(s)")

    def printVehiclesBySeat(self, NumberOfPeople):
        for vehicle in self.Vehicles:
            if vehicle.checkSuitability(NumberOfPeople) == True:
                vehicle.printVehicle()
                print()

    def printAnnualCost(self):
        BranchCost = 0
        counter = 1
        print(f"Vehicles at Branch with ID {self.BranchID}:")
        for vehicle in self.Vehicles:
            print(f"Vehicle {counter}:")
            if vehicle.getObjectType() == "Car":
                km = float(input("Enter KM of the car: "))
                BranchCost += vehicle.annualCost(km)
            else:
                maintenanceCost = float(input("Enter the maintenanceCost of the Bus: "))  
                NumberOfTimesServiced = int(input("Enter the Number of Times that the Bus Serviced: "))
                BranchCost += vehicle.annualCost(maintenanceCost, NumberOfTimesServiced)
            counter += 1
        print(f"Total Annual Cost for Branch with ID: {self.BranchID} is {BranchCost}\n")
        return BranchCost
