# main.py

import pandas as pd
from strategies.sma import SMA
from strategies.ema import EMA
from strategies.momentum import Momentum
from simulator.simulator import Simulator
from visualization.plot import plot_results

def main():
    # Load historical price data
    data = pd.read_csv('data/historical_prices.csv')  # Ensure you have this CSV file

    # Initialize strategies
    sma_strategy = SMA(data)
    ema_strategy = EMA(data)
    momentum_strategy = Momentum(data)

    # Initialize simulator
    simulator = Simulator()

    # Run simulations
    sma_results = simulator.run(sma_strategy)
    ema_results = simulator.run(ema_strategy)
    momentum_results = simulator.run(momentum_strategy)

    # Visualize results
    plot_results(sma_results, 'SMA Strategy Results')
    plot_results(ema_results, 'EMA Strategy Results')
    plot_results(momentum_results, 'Momentum Strategy Results')

if __name__ == "__main__":
    main()