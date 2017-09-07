if __name__=="store":
    class Store(object):
        def __init__(self, location, owner):
            self.products = []
            self.location = location
            self.owner = owner
        def add_product(self, product):
            self.products.append(product)
            return self
        def remove_product(self, productname):
            for x in self.products:
                if x.name == productname:
                    self.products.remove(x)
            return self
        def inventory(self):
            for x in self.products:
                x.display_info()
            return self
        def __repr__(self):
            return "<Store object Products: {} Location: {} Owner: {}>".format(self.products, self. location, self.owner)