
"""
created class Promotion, with 3 subclasses of different promotions,
return amount of discount
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name, percent=None):
        self.name = name
        self.percent = percent

    @abstractmethod
    def apply_promotion(self, product):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity > 1:
            discounted_amount = (product.price / 2) * (int(quantity / 2))
        else:
            discounted_amount = 0

        return discounted_amount


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity > 1:
            discounted_amount = product.price * (int(quantity / 3))
        else:
            discounted_amount = 0

        return discounted_amount


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_amount = (product.price * self.percent / 100) * quantity
        return discounted_amount
