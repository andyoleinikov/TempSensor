from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, load_only
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


def add_temp(location_name, temperature, source, dt=None, commit=False):
    dt = dt or datetime.now()
    temp = Temp(location_name, temperature, source, dt )
    db_session.add(temp) 
    if commit:
        db_session.commit()

def get_t_range(source='gismeteo', date_range=datetime(2016, 10, 7, 00, 00, 00, 000000)):
    t_range = []
    for date in date_range:
        this_temp = Temp.query.filter(Temp.source == source, Temp.date == date).options(load_only('date', 'temperature')).first().temperature
        t_range.append(this_temp) 
    return t_range

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
