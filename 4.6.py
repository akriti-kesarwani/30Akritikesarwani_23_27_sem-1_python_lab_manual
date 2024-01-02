class LU:
    def display_LU(self):
        print("LU Class")

class ITM:
    def display_ITM(self):
        print("ITM Class")

class Derived(LU, ITM):
    pass


derived_object = Derived()
derived_object.display_LU()
derived_object.display_ITM()