if __name__=="underscore":
    class Underscore(object):
        def map(self, l, iteratee):
            for x in xrange(len(l)):
                l[x] = iteratee(l[x])
            return l
        def reduce(self, l, iteratee, *memo):
            if not memo:
                memo = l[0]
                l.pop(0)
            while len(l)>0:
                memo = iteratee(memo, l[0])
                l.pop(0)
            return memo
        def find(self, l, predicate):
            for x in l:
                if predicate(x):
                    return x
        def filter(self, l, predicate):
            newl = []
            for x in l:
                if predicate(x):
                    newl.append(x)
            return newl
        def reject(self, l, predicate):
            newl = []
            for x in l:
                if not predicate(x):
                    newl.append(x)
            return newl
        def __repr__(self):
            return "<Underscore object. Module with 5 functions>"
# _ = Underscore()
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print evens
# triple = _.map([1, 2, 3, 4, 5, 6], lambda x: x*3)
# print triple
# sumall = _.reduce([1, 2, 3, 4, 5, 6], lambda memo,x: memo+x)
# print sumall
# firsteven = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print firsteven
# removeeven = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print removeeven