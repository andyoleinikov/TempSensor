import numpy as np
import matplotlib as mpl

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm

import datetime as dt

dates = [
    dt.datetime(2000, 3, 2),
    dt.datetime(2000, 3, 3),
    dt.datetime(2000, 3, 4),
    dt.datetime(2000, 3, 5),
    dt.datetime(2000, 3, 6),
    dt.datetime(2000, 3, 7),
]

rates = [
    1.25,
    1.2,
    1.3,
    1.4,
    1.1,
    1.3,
]


fig, ax = plt.subplots()

ax.plot_date(dates, rates, '-b')

ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

fig.autofmt_xdate()

ax.grid(True)

plt.show()