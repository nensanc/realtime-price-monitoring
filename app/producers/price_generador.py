import random

class VegetablePriceSimulator:
    def __init__(self):
        self.vegetables = [
            "tomato", "onion", "lettuce", "carrot", "cucumber",
            "spinach", "broccoli", "pepper", "eggplant", "zucchini",
            "potato", "garlic", "cabbage", "cauliflower", "celery"
        ]
        # Initialize base prices for each vegetable
        self.prices = {veg: round(random.uniform(1.0, 3.0), 2) for veg in self.vegetables}

    def next(self):
        """
        Simulate the next time step in the price series.
        Each price changes slightly (random walk).
        Returns a dictionary with updated prices.
        """
        for veg in self.vegetables:
            # Simulate a small percentage change, e.g., -2% to +2%
            change_pct = random.uniform(-0.02, 0.02)
            new_price = self.prices[veg] * (1 + change_pct)
            # Clamp price between $0.5 and $5.0
            self.prices[veg] = round(max(0.5, min(new_price, 5.0)), 2)
        return self.prices.copy()

# Example usage
if __name__ == "__main__":
    simulator = VegetablePriceSimulator()
    for _ in range(10):  # Generate 10 time steps
        print(simulator.next())