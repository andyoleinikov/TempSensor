import matplotlib as mpl
mpl.use('Agg')
from mpld3 import plugins
import mpld3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as fm
import datetime as dt 
from dateutil.relativedelta import  relativedelta

from tdb import get_item_range
from forecast import get_weather_lists

def plot_forecast(ax, date):
    plot_condition_date = relativedelta(days=2)
    if date < dt.datetime.now()+ plot_condition_date and date > dt.datetime.now() - plot_condition_date:
        forecast_dates, forecast_temps = get_weather_lists()
        return ax.plot_date(forecast_dates, forecast_temps, '-', label='forecast')


def plot_db_data(ax, date):
    for source in ['gismeteo', 'RPI_sensor']:
        year_delta = 0
        date_ = date
        while date_ > dt.datetime(2014, 6, 7, 00, 00, 00, 000000):
            date_range = get_item_range(item='date', source=source, date=date_)
            if not date_range:
                date_ -= relativedelta(years=1)
                year_delta += 1
                continue
            label_year = dt.datetime.strftime(date_range[0], '%Y')
            date_range = [d + relativedelta(years=1 * year_delta) for d in date_range]
            t_range = get_item_range(item='temperature', source = source, date=date_)
            ax.plot_date(date_range, t_range, '-', label='%s %s' % (source, label_year))
            date_ -= relativedelta(years=1)
            year_delta += 1


def plot_grid(fig, ax):
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    axes = plt.gca()
    axes.set_ylim([-30,30])

    fig.autofmt_xdate()

    ax.grid(True)


def get_plot(date=dt.datetime.now(), output='html'):
    
    fig, ax = plt.subplots(figsize=(10, 4))

    plot_db_data(ax, date)
        
    plot_forecast(ax, date)

    plot_grid(fig, ax)
    
    handles, labels = ax.get_legend_handles_labels()

    if output == 'html':
        interactive_legend = plugins.InteractiveLegendPlugin(handles, labels)
        plugins.connect(fig, interactive_legend)
        fig.subplots_adjust(right=0.7)
        plot_html = mpld3.fig_to_html(fig, template_type='general')
        return plot_html
    
    else:
        ax.legend(handles, labels)
        plt.savefig('./static/graph/graph.png')
        plt.close()
        f = open('./static/graph/graph.png', 'rb')  # some file on local disk
        return f


if __name__ == '__main__':
    get_plot(date=dt.datetime.now(), output='img')