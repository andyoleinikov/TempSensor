
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
    
    fig, ax = plt.subplots()

    for source in ['gismeteo', 'RPI_sensor']:
        year_delta = 0
        date_ = date
        while date_ > dt.datetime(2014, 6, 7, 00, 00, 00, 000000):
            date_range = get_item_range(item='date', source = source, date=date_)
            if not date_range:
                date_ -= dt.timedelta(days=365)
                year_delta += 1
                continue
            year = date_range[0]
            date_range = [d + dt.timedelta(days=365 * year_delta) for d in date_range]
            t_range = get_item_range(item='temperature', source = source, date=date_)
            ax.plot_date(date_range, t_range, '-', label = '%s %s' % (source, year))
            date_ -= dt.timedelta(days=365)
            year_delta += 1

    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    # print(handles, labels)
    # interactive_legend = plugins.InteractiveLegendPlugin(
    #     zip(handles, ax.collections),
    #     labels,
    #     alpha_unsel=0.5,
    #     alpha_over=1.5, 
    #     start_visible=True,
    # )
    # plugins.connect(fig, interactive_legend)

    fig.autofmt_xdate()

    ax.grid(True)
    ax.legend()

    plot_html = mpld3.fig_to_html(fig, template_type='general')


    return plot_html


# mpld3.show()
