from branch import Branch

class Company:
    def __init__(self, Name="Undefined", NumberOfBranches=0):
        self.Name = Name
        self.Branches = []
        self.NumberOfBranches = NumberOfBranches
    
    def getBranchIDList(self):
        IDList = []
        for branch in self.Branches:
            IDList.append(branch.getBranchID())
        return IDList

    def addBranch(self):
        branch = Branch()
        branch.BranchID = int(input("Please enter branch's ID: "))
        branch.City = input("Please enter the city, where branch is located: ")
        self.Branches.append(branch)

    def printBranches(self):
        for branch in self.Branches:
            branch.printBranch()

    def printVehicles(self):
        for branch in self.Branches:
            branch.printVehicles()

    def printVehiclesByType(self, choice):
        for branch in self.Branches:
            branch.printVehiclesByType(choice)

    def printTypeStatistics(self):
        for branch in self.Branches:
            branch.printTypeStatistics()

    def printVehiclesBySeat(self, NumberOfPeople):
        for branch in self.Branches:
            branch.printVehiclesBySeat(NumberOfPeople)

    def printAnnualCost(self):
        CompanyCost = 0
        for branch in self.Branches:
            CompanyCost += branch.printAnnualCost()
        print("------------------------------")
        print(f"Total Annual Cost for Quick Transport is {CompanyCost}\n")
            