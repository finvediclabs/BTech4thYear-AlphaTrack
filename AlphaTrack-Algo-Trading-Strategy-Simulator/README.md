# AlphaTrack: Algo Trading Strategy Simulator

## Overview
AlphaTrack is an algorithmic trading strategy simulator designed to help users understand and visualize various trading strategies, including Simple Moving Average (SMA), Exponential Moving Average (EMA), and Momentum strategies. This project provides a framework for simulating these strategies on historical price data and visualizing the results.

## Project Structure
```
AlphaTrack-Algo-Trading-Strategy-Simulator
├── src
│   ├── main.py
│   ├── strategies
│   │   ├── sma.py
│   │   ├── ema.py
│   │   └── momentum.py
│   ├── simulator
│   │   └── simulator.py
│   └── visualization
│       └── plot.py
├── requirements.txt
└── README.md
```

## Installation
To get started with AlphaTrack, clone the repository and install the required dependencies. You can do this by running the following commands in your terminal:

```bash
git clone <repository-url>
cd AlphaTrack-Algo-Trading-Strategy-Simulator
pip install -r requirements.txt
```

## Running the Simulator
To run the trading strategy simulator, execute the following command:

```bash
python src/main.py
```

This will initialize the simulation and start the main loop, allowing you to test different trading strategies.

## Resolving Common Bugs
While working with AlphaTrack, you may encounter some common issues. Here are some troubleshooting tips:

1. **Module Not Found Error**: Ensure that you are running the script from the root directory of the project. If you are in the `src` directory, you may need to adjust your import statements.

2. **Dependency Issues**: If you encounter errors related to missing packages, double-check that you have installed all the dependencies listed in `requirements.txt`. You can reinstall them using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Data Loading Errors**: If the simulator fails to load historical price data, verify that the data file is in the correct format and located in the expected directory.

4. **Visualization Errors**: If the plots do not display correctly, ensure that you have the necessary libraries installed (e.g., matplotlib). You can also check for any errors in the data being passed to the plotting functions.

5. **Performance Issues**: If the simulation runs slowly, consider optimizing your code or reducing the amount of historical data being processed.

For further assistance, please refer to the documentation in the source files or open an issue in the repository. Happy trading!