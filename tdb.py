from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, load_only
from sqlalchemy.ext.declarative import declarative_base
import datetime  as dt



def add_temp(location_name, temperature, source, date=None, commit=False):
    if date:
        temp = Temp(location_name, temperature, source, date )
    else:
        date = dt.datetime.now()
        temp = Temp(location_name, temperature, source, date )
    db_session.add(temp) 
    if commit:
        db_session.commit()

def get_item_range(item='temperature', source='gismeteo',
        date=dt.datetime(2016, 10, 7), shift=dt.timedelta(days=7)):
    date_from = date - shift
    date_to = date + shift
    db_range = Temp.query.filter(
        Temp.source == source,
        Temp.date > date_from,
        Temp.date <= date_to,
    ).options(load_only(item)).order_by(
        Temp.date
    ).all()
    item_range = []
    for date in db_range:
        item_range.append(getattr(date, item))
    return item_range

engine = create_engine('sqlite:///weather.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Temp(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    location_name = Column(String(50))
    temperature = Column(Float)
    source = Column(String(120))
    date = Column(DateTime)

    def __init__(self, location_name=None, temperature=None, source=None, date=None):
        self.location_name = location_name
        self.temperature = temperature
        self.source = source
        self.date = date

    def __repr__(self):
        return '<{}, {}, {}, {} >'.format(self.location_name, self.temperature, self.source, self.date)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
