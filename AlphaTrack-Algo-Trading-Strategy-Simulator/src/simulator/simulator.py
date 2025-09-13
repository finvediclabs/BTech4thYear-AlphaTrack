class Simulator:
    def __init__(self, strategy, initial_capital=10000):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.balance = initial_capital
        self.positions = []
        self.performance = []

    def run_simulation(self, historical_data):
        for index, row in historical_data.iterrows():
            self._apply_strategy(row)

    def _apply_strategy(self, row):
        signal = self.strategy.generate_signal(row)
        if signal == 'buy' and self.balance > 0:
            self._buy(row['price'])
        elif signal == 'sell' and self.positions:
            self._sell(row['price'])

    def _buy(self, price):
        shares = self.balance // price
        self.positions.append(shares)
        self.balance -= shares * price

    def _sell(self, price):
        shares = self.positions.pop()
        self.balance += shares * price

    def get_performance(self):
        return {
            'final_balance': self.balance,
            'positions': self.positions,
            'performance': self.performance
        }