class Package:
    # creates a class called Package
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status_quo):
        self.ID = ID
        # assigns id to id
        self.address = address
        # assigns address to address
        self.city = city
        # assigns city to city
        self.state = state
        # assigns state to state
        self.zipcode = zipcode
        # assigns zip_code to zip_code
        self.deadline = deadline
        # assigns deadline to deadline
        self.weight = weight
        # assigns weight to weight
        self.status_quo = status_quo
        # assigns status_quo to status_quo
        self.departure_time = None
        # assigns None initially to departure_time
        self.delivery_time = None
        # assigns None initially to departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline, self.weight, self.delivery_time,
                                                       self.status_quo)

    # the above __str__ method represents the Package class instances as strings
    # O(n)
    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            # if delivery_time is less than timedelta
            self.status_quo = "Delivery completed"
            print("Delivery completed at:", self.delivery_time)
            # then status_quo is set to Delivery Complete
        elif self.departure_time > convert_timedelta:
            # if departure_time is greater than timedelta
            self.status_quo = "En route to destination"
            # then status_quo is set to En Route to Destination
        else:
            self.status_quo = "At Hub awaiting pickup"
