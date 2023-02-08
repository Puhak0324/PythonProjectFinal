class DeliveryTruck:
    # creates a class that defines DeliveryTruck
    def __init__(self, capacity, speed, current_load, packages, mileage, address, depart_time):
        self.capacity = capacity
        # assigns capacity to capacity
        self.speed = speed
        # assigns speed to speed
        self.current_load = current_load
        # assigns current_load to current_load
        self.packages = packages
        # assigns packages to packages
        self.mileage = mileage
        # assigns mileage to mileage
        self.address = address
        # assigns address to address
        self.depart_time = depart_time
        # assigns depart_time to depart_time
        self.time = depart_time
        # assigns depart_time to time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.current_load, self.packages,
                                               self.mileage, self.address, self.depart_time)
    # converts all selected instances of the Deliverytruck class to strings
