if __name__=="hospital":
    class Patient(object):
        def __init__(self, idnum, name, allergies):
            self.idnum = idnum
            self.name = name
            self.allergies = allergies
            self.bednumber = None
        def __repr__(self):
            return "<Patient object ID#: {} Name: {} Allergies: {} Bed#: {}>".format(self.idnum, self.name, self.allergies, self.bednumber)
    class Hospital(object):
        def __init__(self, name, capacity):
            self.name = name
            self.capacity = capacity
            self.patients = []
        def admit(self, patient):
            def empty_bed():
                for x in xrange(1, self.capacity+1):
                    empty = True
                    for y in self.patients:
                        if x == y.bednumber:
                            empty = False
                    if empty:
                        return x
            if len(self.patients)<self.capacity:
                patient.bednumber = empty_bed()
                self.patients.append(patient)
                print "Admission is complete"
            else:
                print "Hospital is full"
            return self
        def discharge(self, *patientname):
            if patientname:
                for x in self.patients:
                    if x.name == patientname:
                        x.bednumber = None
                        self.patients.remove(x)
                        print "Discharge is complete"
            else:
                for x in self.patients:
                    print x.name
            return self
        def __repr__(self):
            return "<Hospital object Name: {} Capacity: {} Patients: {}".format(self.name, self.capacity, self.patients)