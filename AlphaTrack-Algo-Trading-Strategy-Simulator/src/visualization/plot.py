def plot_results(simulation_data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(14, 7))

    # Plotting the price data
    plt.plot(simulation_data['dates'], simulation_data['prices'], label='Price', color='blue')

    # Plotting the strategy signals
    if 'sma_signals' in simulation_data:
        plt.plot(simulation_data['dates'], simulation_data['sma_signals'], label='SMA Signals', color='orange')

    if 'ema_signals' in simulation_data:
        plt.plot(simulation_data['dates'], simulation_data['ema_signals'], label='EMA Signals', color='green')

    if 'momentum_signals' in simulation_data:
        plt.plot(simulation_data['dates'], simulation_data['momentum_signals'], label='Momentum Signals', color='red')

    plt.title('Trading Strategy Simulation Results')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()