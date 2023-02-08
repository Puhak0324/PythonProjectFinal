# Austin Puhak ID 010500702
import csv
import datetime
import Truck

from Hash_Table import ChainingHashTable
from Package import Package

# Read the file of distance information
with open("Distance_File.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file of address information
with open("Address_File.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)

# Read the file of package information
with open("Package_File.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)


# all three CSV files were created from the WGU Excel files


# Create package objects from the CSV package file
# Load package objects into the hash table: package_hash_table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        # This runs in O(n) time/space complexity as it cycles through each element
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub awaiting pickup"

            # Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # Insert data into hash table
            package_hash_table.insert(pID, p)


# Method for finding distance between two addresses O(1) complexity
def distance_in_between(x_value, y_value):
    distance = CSV_Distance[x_value][y_value]
    if distance == '':
        distance = CSV_Distance[y_value][x_value]

    return float(distance)


# Method to get address number from string literal of address
def extract_address(address):
    # This runs in O(n) complexity as it cycles through each row
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Create truck object truck1
truck1 = Truck.DeliveryTruck(16, 18, None, [1, 12, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                             datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck.DeliveryTruck(16, 18, None, [3, 6, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                             "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck.DeliveryTruck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                             datetime.timedelta(hours=9, minutes=5))

# Create hash table
package_hash_table = ChainingHashTable()

# Load packages into hash table
load_package_data("Package_File.csv", package_hash_table)


# Method for ordering packages on a given truck using the nearest neighbor algo
def delivering_packages(truck):
    # All packages placed into array of not delivered
    not_delivered = []
    # This runs in O(n) complexity as it cycles through each package ID
    for packageID in truck.packages:
        package = package_hash_table.search(packageID)
        not_delivered.append(package)
    # Clear the package list of a given truck so the packages can be placed back into the truck in the order
    # of the nearest neighbor
    truck.packages.clear()

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    # This portion operates in O(nlogn)complexity (for loop nested in while loop)
    while len(not_delivered) > 0:
        next_address = 2000
        next_package = None
        for package in not_delivered:
            if distance_in_between(extract_address(truck.address), extract_address(package.address)) <= next_address:
                next_address = distance_in_between(extract_address(truck.address), extract_address(package.address))
                next_package = package
        # Removes the same package from the not_delivered list
        not_delivered.remove(next_package)

        # Adds next closest package to the truck package list
        truck.packages.append(next_package.ID)

        # Takes the mileage driven to this package into the truck.mileage attribute
        truck.mileage += next_address

        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address

        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)

        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


# Put the trucks through the loading process
delivering_packages(truck1)
delivering_packages(truck2)
# The below line of code ensures that truck 3 does not leave until either of the first two trucks are finished
# delivering their packages
truck3.depart_time = min(truck1.time, truck2.time)
delivering_packages(truck3)


class Main:
    # User Interface
    # Upon running the program, the below message will appear.
    print("Western Governors University Parcel Service (WGUPS)")
    # The user will be asked to start the process by entering the word "password".
    # user is given three chances before account is locked to simulate real world.
    password_input = input("To start please enter password: ")
    if password_input != "password":
        print("Please try again: ")
        password_input = input()
    if password_input != "password":
        print("Hint: the password is password")
        password_input = input()
    if password_input == "password":
        # once password is entered, it asks user if they want to view total mileage for route.
        mileage_input = input("Would you like to view the current route mileage? ")
        if mileage_input == "yes":
            # If yes, print total mileage for all trucks and what packages are assigned to each specific truck.
            print("The mileage for the current route is:", (truck1.mileage + truck2.mileage + truck3.mileage),
                  "miles")
            print("Truck 1 is assigned packages with ID: ", truck1.packages)
            print("Truck 2 is assigned packages with ID: ", truck2.packages)
            print("Truck 3 is assigned packages with ID: ", truck3.packages)
            # User is then asked if they want to check the status of a specific package.
            package_input = input("Would you like to check the status of a specific package(s)? ")
            if package_input == "yes":
                # If yes, the user will be asked to enter a specific time using the following format
                time_input = input(
                    "Please enter a time to check status of package(s). (Use the following format, HH:MM:SS). "
                    "\nSelected Time: ")
                (h, m, s) = time_input.split(":")
                # assigns the entered time into hours, minutes, and seconds.
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # The user will be asked if they want to see the status of all packages or only one
                print("To view the status of an individual package please type 'single'. To display all"
                      " packages please type 'all'.")
                selection_input = input("Selection: ")
                # If the user enters "solo" the program will ask for one package ID
                if selection_input == "single":
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    solo_input = input("Enter the numeric package ID: ")
                    package = package_hash_table.search(int(solo_input))
                    package.update_status(convert_timedelta)
                    print(str(package))
                    print("Would you like to view another package? ")
                    another_input = input()
                    while another_input == "yes":
                        package_id_input = input("Enter the numeric package ID: ")
                        package2 = package_hash_table.search(int(package_id_input))
                        package2.update_status(convert_timedelta)
                        print(str(package2))
                        print("Would you like to view another package? ")
                        another_input = input()

                        if another_input == "no":
                            print("Process Complete. Closing program.")
                            exit()
                # If the user types "all" the program will display all package information at once
                elif selection_input == "all":
                    for packageID in range(1, 41):
                        package = package_hash_table.search(packageID)
                        package.update_status(convert_timedelta)
                        print(str(package))
                    print("Process Complete. Closing program.")
                    exit()
                else:
                    selection_input != "single"
                    selection_input != "all"
                    print("Invalid entry. closing program.")
                    exit()
            else:
                package_input != "yes"
                print("Invalid entry. closing program.")
                exit()
        else:
            mileage_input != "yes"
            print("Invalid entry. closing program.")
            exit()
    elif password_input != "password":
        print("Invalid entry. Your account has now been locked.")
        print("For account recovery, please contact WGU at (877)-435-7948.")
        exit()
