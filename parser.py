from bs4 import BeautifulSoup
from req import get_html
from datetime import datetime
from tdb import Temp, db_session, add_temp
import time


# сделать через dateutil and datetime
def t_from_text(text):
        return float(text.replace('+', ''))



for year in range(2014, 2018):
    for month in  range(1,13):
        html = get_html("https://www.gismeteo.ru/diary/168669/%s/%s/" % (year, month))
        if html == False:
            print('no more data')
            break
        bs = BeautifulSoup(html, 'html.parser')

        try:
            items = bs.find('div', id='data_block').find('table').find_all('tr')
        except AttributeError as e:
            continue

        for item in items:
            day = item.find('td', class_='first')
            temp = item.find_all('td', class_='first_in_group')
            if not day or len(temp) < 2:
                continue
            actual_date_morning = datetime(year, month, int(day.text), 6)
            actual_date_evening = datetime(year, month, int(day.text), 21)
            morning, evening, *_ = temp
            if morning.text: 
                add_temp("Zapolitsy", t_from_text(morning.text), "gismeteo", actual_date_morning)   
            else:
                continue

            if evening.text: 
                add_temp("Zapolitsy", t_from_text(evening.text), "gismeteo", actual_date_evening)   
            else:
                continue

        print('month ok' + str(month))      
    db_session.commit()
    print('year ok' + str(year))  
    time.sleep(5) 

