import math


def calculate_discounted_price(price: int, discount_rate: float) -> int:
    return math.ceil(price * (1 - discount_rate))
