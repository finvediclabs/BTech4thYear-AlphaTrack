class EMA:
    def __init__(self, period):
        self.period = period

    def calculate(self, prices):
        if len(prices) < self.period:
            return []

        ema_values = []
        multiplier = 2 / (self.period + 1)
        ema_values.append(sum(prices[:self.period]) / self.period)  # Initial SMA for the first EMA value

        for price in prices[self.period:]:
            new_ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
            ema_values.append(new_ema)

        return ema_values

    def apply_strategy(self, prices):
        signals = []
        ema_values = self.calculate(prices)

        for i in range(len(prices)):
            if i < self.period - 1:
                signals.append(0)  # No signal until we have enough data
            elif prices[i] > ema_values[i - (self.period - 1)]:
                signals.append(1)  # Buy signal
            else:
                signals.append(-1)  # Sell signal

        return signals