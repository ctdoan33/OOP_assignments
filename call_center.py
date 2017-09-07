if __name__=="call_center":
    import random
    class Call(object):
        def __init__(self, name, phone_number, time, reason):
            self.uniqueid = int(random.random()*1000000)
            self.name = name
            self.phone_number = phone_number
            self.time = time
            self.reason = reason
        def display(self):
            print self.uniqueid
            print self.name
            print self.phone_number
            print self.time
            print self.reason
            return self
        def __repr__(self):
            return "<Call object ID#: {} Caller: {} Number: {} Time: {} Reason: {}>".format(self.uniqueid, self.name, self.phone_number, self.time, self.reason)
    class CallCenter(object):
        def __init__(self):
            self.calls = []
            self.queue_size = 0
        def add(self, call):
            self.calls.append(call)
            self.queue_size += 1
            return self
        def remove(self, *phone):
            if phone:
                for x in self.calls:
                    if x.phone_number in phone:
                        self.calls.remove(x)
            else:
                self.calls.pop(0)
            self.queue_size -= 1
            return self
        def sort_by_time(self):
            def get_time(x):
                return x.time
            self.calls.sort(key=get_time)
            return self
        def info(self):
            for x in self.calls:
                print x.name, x.phone_number
            print self.queue_size
            return self
        def __repr__(self):
            return "<CallCenter object Calls: {} In queue: {}>".format(self.calls, self.queue_size)