from company import Company

def menu():
    print("\nOptions:")
    print("1. Add a new branch to the company.")
    print("2. Add a new vehicle (car or bus) to a branch.")
    print("3. Print all the branches along with their cities and the number of vehicles.")
    print("4. Print the details stored as member variables for the vehicles in each branch.")
    print("5. Print the details stored as member variables for the vehicles in each branch whose type is a given type.")
    print("6. Print the number of each type of vehicle in each branch.")
    print("7. Print the details stored as member variables for the vehicles that can carry a given number of people in each branch.")
    print("8. Calculate the total annual cost for the company.")
    print("9. Exit")

def main():
    option = 0
    myCompany = Company("Quick Transports", 10)
    print("\nWelcome to Quick Transports")
    while (option != 9):
        menu()
        option = int(input("Your selection: "))

        if option == 1:
            myCompany.addBranch()
            
        elif option == 2:
            branchID = int(input("Please enter the ID of the Branch: "))
            IDList = myCompany.getBranchIDList()
            if branchID not in IDList:
                print(f"There is no branch with ID {branchID} at Quick Transport")
            else:
                for branch in myCompany.Branches:
                    if branch.getBranchID() == branchID:
                        branch.addVehicle()
            
        elif option == 3:
            print()
            myCompany.printBranches()
        
        elif option == 4:
            print()
            myCompany.printVehicles()
        
        elif option == 5:
            print("Please select the type of the vehicles, You want to see: (0) Bus, (1) Car")
            choice = int(input("Your choice: "))
            myCompany.printVehiclesByType(choice)
        
        elif option == 6:
            print()
            myCompany.printTypeStatistics()

        elif option == 7:
            numOfPassengers = int(input("Please enter the number of passengers vehicle should be able to carry: "))
            print()
            myCompany.printVehiclesBySeat(numOfPassengers)
        
        elif option == 8:
            myCompany.printAnnualCost()

        elif option == 9:
            print("Byeee!")

        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()