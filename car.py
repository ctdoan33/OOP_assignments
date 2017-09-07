if __name__=="car":
    class Car(object):
        def __init__(self, price, speed, fuel, mileage):
            self.price = price
            self.speed = speed
            self.fuel = fuel
            self.mileage = mileage
            if price>10000:
                self.tax = 0.15
            else:
                self.tax = 0.12
            self.display_all()
        def display_all(self):
            print "Price:", self.price
            print "Speed:", self.speed
            print "Fuel:", self.fuel
            print "Mileage:", self.mileage
            print "Tax:", self.tax
            return self
        def __repr__(self):
            return "<Car object Price: {} Speed: {} Fuel: {} Mileage: {} Tax: {}>".format(self.price, self.speed, self.fuel, self.mileage, self.tax)