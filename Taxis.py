
from taxi import Taxi


def main():
    Taxi.price_per_km=1.2
    taxi1=Taxi("Prius 1", 100, 1.2)
    taxi1.drive(40)
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1.__str__())

main()