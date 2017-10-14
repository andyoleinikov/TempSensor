import mpld3
from mpld3 import plugins

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm


from tdb import engine, Temp, get_t_range
import datetime as dt 
from dateutil import rrule





def get_date_range(date=dt.datetime.now()):
    date_range = list(rrule.rrule(rrule.DAILY, count = 10, dtstart=(date + dt.timedelta(days = 5))))
    return date_range






date_range = get_date_range(dt.datetime(2016, 10, 7))
t_range = get_t_range(date_range=date_range)

date_range1 = get_date_range(dt.datetime(2015, 10, 7))
t_range1 = get_t_range(date_range=date_range)

print(date_range)
print(t_range)

fig, ax = plt.subplots()

ax.plot_date(date_range, t_range, '-b')

ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

fig.autofmt_xdate()

ax.grid(True)

# plt.show()

plot_html = mpld3.fig_to_html(fig, template_type='general')

# mpld3.show()