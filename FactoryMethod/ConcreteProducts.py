from ProductInterface import Transport
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box."

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a container."
