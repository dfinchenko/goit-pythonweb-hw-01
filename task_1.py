from abc import ABC, abstractmethod
import logging
from typing import Type

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Створення транспортних засобів для США
us_factory = USVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()

# Створення транспортних засобів для ЄС
eu_factory = EUVehicleFactory()

eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_car.start_engine()

eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")
eu_motorcycle.start_engine()