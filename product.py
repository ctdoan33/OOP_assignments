if __name__=="product":
    class Product(object):
        def __init__(self, price, name, weight, brand, cost):
            self.price = price
            self.name = name
            self.weight = weight
            self.brand = brand
            self.cost = cost
            self.status = "for sale"
        def sell(self):
            self.status = "sold"
            return self
        def add_tax(self, tax):
            self.price += tax
            return self.price
        def returned(self, reason):
            if self.status == "for sale":
                print "not sold yet"
            elif reason == "defective":
                self.status = "defective"
                self.price = 0
            elif reason == "in the box":
                self.status = "for sale"
            elif reason == "opened":
                self.status = "used"
                self.price *= .8
            return self
        def display_info(self):
            print "Price:", self.price
            print "Item Name:", self.name
            print "Weight:", self.weight
            print "Brand:", self.brand
            print "Cost:", self.cost
            print "Status:", self.status
            return self
        def __repr__(self):
            return "<Product object Price: {} Name: {} Weight: {} Brand: {} Cost: {} Status: {}>".format(self.price, self.name, self.weight, self.brand, self.cost, self.status)