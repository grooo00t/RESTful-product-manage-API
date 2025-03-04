from src.utils.calculations import calculate_discounted_price


class TestCalculations:
    def test_calculate_discounted_price(self):
        assert calculate_discounted_price(10000, 0.1) == 9000

    def test_calculate_discounted_price_under_one(self):
        assert calculate_discounted_price(1, 0.1) == 1
