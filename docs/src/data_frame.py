#! /usr/bin/env python3

import numpy as np
import pandas as pd


def get_stock_by_symbol(name=None):
    if name is None:
        return None
    # This is risky code!  What if the stock symbol passed in does not exist?
    # Silently return an empty frame
    return stock_data_frame.query(f"Name == '{name}'")


stock_data_file = "../../Lecture/all_stocks_5yr.csv"
stock_data_frame = pd.read_csv(stock_data_file)
print(stock_data_frame.info())
print(stock_data_frame.columns)
print(stock_data_frame.head(10))
stock = get_stock_by_symbol(name="GOOG")
print(stock)
print(np.mean(stock))
