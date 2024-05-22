from  dataclasses import dataclass

from model.product import Product


@dataclass
class Connessione:
    p1: Product
    p2: Product
    peso: int
    def __hash__(self):
        return hash(self.p1.Product_number)

    def __str__(self):
        return f"{self.p1.Product} - {self.p2.Product}"
