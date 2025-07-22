import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MonteCarloBacktester:
    def __init__(self, strategy, initial_capital=100000):
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.results = pd.DataFrame()

    def total_signal(df, current_candle):
        current_pos = df.index.get_loc(current_candle)
        c0 = df["Open"].iloc[current_pos] > df["Close"].iloc[current_pos]
        c1 = df["High"].iloc[current_pos] > df["High"].iloc[current_pos]
