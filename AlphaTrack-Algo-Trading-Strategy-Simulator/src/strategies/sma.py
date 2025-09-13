class SMA:
    def __init__(self, window):
        self.window = window

    def calculate(self, prices):
        if len(prices) < self.window:
            return []
        return [sum(prices[i:i + self.window]) / self.window for i in range(len(prices) - self.window + 1)]

    def apply_strategy(self, prices):
        sma_values = self.calculate(prices)
        signals = []
        for i in range(len(sma_values)):
            if prices[i + self.window - 1] > sma_values[i]:
                signals.append(1)  # Buy signal
            elif prices[i + self.window - 1] < sma_values[i]:
                signals.append(-1)  # Sell signal
            else:
                signals.append(0)  # Hold signal
        return signals