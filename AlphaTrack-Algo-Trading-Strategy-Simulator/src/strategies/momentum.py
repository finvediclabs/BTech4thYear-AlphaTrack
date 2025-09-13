class Momentum:
    def __init__(self, window=14):
        self.window = window

    def calculate_momentum(self, prices):
        if len(prices) < self.window:
            raise ValueError("Not enough data to calculate momentum.")
        return prices[-1] - prices[-self.window]

    def apply_strategy(self, prices):
        momentum_values = []
        for i in range(self.window, len(prices)):
            momentum = self.calculate_momentum(prices[:i])
            momentum_values.append(momentum)
        return momentum_values