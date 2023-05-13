#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
stock = get_stock_by_symbol(name="GOOG")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d"))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=90))
plt.gcf().autofmt_xdate()
plt.plot(pd.to_datetime(stock["date"].values), stock["high"].values)
plt.plot(pd.to_datetime(stock["date"].values), stock["low"].values)
plt.legend(["high", "low"])
plt.xlabel("Dates")
plt.ylabel("Price ($)")
plt.title(f"Stock High and Low of {stock['Name'].values[0]}")
plt.grid(True)
plt.show()
