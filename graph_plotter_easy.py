import mpld3
from mpld3 import plugins

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm


from tdb import get_item_range
import datetime as dt 
from dateutil import rrule






def get_plot_html(source='gismeteo', date=dt.datetime(2016, 10, 7, 00, 00, 00, 000000)):
    date_range = get_item_range(item='date', source= source, date=date)
    t_range = get_item_range(item='temperature', source= source, date=date)
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

    return plot_html


# mpld3.show()