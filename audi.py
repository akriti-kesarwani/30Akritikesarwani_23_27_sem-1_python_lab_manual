# audi.py

class Audi:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"Audi {self.model}'s engine is started.")

    def drive(self):
        print(f"Driving the Audi {self.model}.")
