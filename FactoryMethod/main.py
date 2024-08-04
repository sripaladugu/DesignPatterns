from CreatorInterface import Logistics
from ConcreteCreators import RoadLogistics, SeaLogistics

def client_code(logistics: Logistics):
    print(logistics.plan_delivery())

if __name__ == "__main__":
    print("App: Launched with RoadLogistics.")
    client_code(RoadLogistics())

    print("\nApp: Launched with SeaLogistics.")
    client_code(SeaLogistics())
