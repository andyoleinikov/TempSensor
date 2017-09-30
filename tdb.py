from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Temp(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    location_name = Column(String(50))
    temperature = Column(Real)
    source = Column(String(120))
    date = Column(DateTime)

    def __init__(self, location_name=None, temperature=None, source=None, date=None):
        self.location_name = location_name
        self.temperature = temperature
        self.source = source
        self.date = date

    def __repr__(self):
        return '<Temp {} {}>'.format(self.location_name, self.temperature, self.source, self.date)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
        self.title = title
        self.image = image
        self.published = published
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post {}>'.format(self.title)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)