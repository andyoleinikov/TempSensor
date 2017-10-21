
import matplotlib as mpl
mpl.use('Agg')
from mpld3 import plugins
import mpld3
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
    ax.plot_date(date_range1, t_range1, '-r')

    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    handles, labels = ax.get_legend_handles_labels() # return lines and labels
    interactive_legend = plugins.InteractiveLegendPlugin(zip(handles, ax.collections),
        labels,
        alpha_unsel=0.5,
        alpha_over=1.5, 
        start_visible=True)
    plugins.connect(fig, interactive_legend)

    fig.autofmt_xdate()

    ax.grid(True)

    # plt.show()

    plot_html = mpld3.fig_to_html(fig, template_type='general')


    return plot_html


# mpld3.show()
