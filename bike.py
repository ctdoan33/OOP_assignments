if __name__=="bike":
    class Bike(object):
        def __init__(self, price, max_speed):
            self.price = price
            self.max_speed = max_speed
            self.miles = 0
        def displayInfo(self):
            print "price:", self.price
            print "max speed:", self.max_speed
            print "total miles: ", self.miles
            return self
        def ride(self):
            print "Riding"
            self.miles += 10
            return self
        def reverse(self):
            if(self.miles>=5): # prevents negative miles
                print "Reversing"
                self.miles -= 5
            else:
                print "Cannot reverse"
            return self
        def __repr__(self):
            return "<Bike object Price: {} Speed: {} Mileage: {}>".format(self.price, self.max_speed, self.miles)