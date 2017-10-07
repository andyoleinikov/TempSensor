from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


def add_temp(name, temperature, device_name, dt=None, commit=False):
    dt = dt or datetime.now()
    temp = Temp(name, temperature, device_name, dt )
    db_session.add(temp) 
    if commit:
        db_session.commit()

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
        return '<Temp {} {}>'.format(self.location_name, self.temperature, self.source, self.date)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)