if __name__=="math_dojo":
    class MathDojo(object):
        def __init__(self):
            self.output = 0
        def add(self, num1, *nums):
            if type(num1)==list or type(num1)==tuple:
                self.output += sum(num1)
            else:
                self.output += num1
            for x in nums:
                if type(x)==list or type(x)==tuple:
                    self.output += sum(x)
                else:
                    self.output += x
            return self
        def subtract(self, num1, *nums):
            if type(num1)==list or type(num1)==tuple:
                self.output -= sum(num1)
            else:
                self.output -= num1
            for y in nums:
                if type(y)==list or type(y)==tuple:
                    self.output -= sum(y)
                else:
                    self.output -= y
            return self
        def result(self):
            return self.output
        def __repr__(self):
            return "<Math Dojo object Current Value: {}>".format(self.output)