
"""
created class Promotion
"""
from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name



    @abstractmethod
    def apply_promotion(self, product):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product):
        print(product)
        if product.quantity >= self.ordered_quantity:
            discounted_amount = (self.ordered_quantity // 2) * (product.price / 2)
        else:
            discounted_amount = 0
        return discounted_amount


