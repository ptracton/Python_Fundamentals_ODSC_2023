#! /usr/bin/env python3

import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(f"Series = {s} dtype = {s.dtype}")
print(s["a"])
print(s * 2)
