from CreatorInterface import Logistics
from ProductInterface import Transport
from ConcreteProducts import Truck, Ship

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
