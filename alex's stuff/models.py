from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Book(Base):
    __tablename__ = 'wine'
    _c0 = COlumn(integer, primary_key=True),
    country= Column(String),
    description= Column(String),
    designation= Column(String),
    points= Column(Integer),
    price = Column(Integer),
    province= Column(String),
    region_1= Column(String),
    region_2= Column(String),
    taster_name= Column(String),
    taster_twitter_handle= Column(String),
    title= Column(String),
    variety= Column(String),
    winery= Column(String),
    
    def __repr__(self):
        return "<Book(country='{}', points='{}', price={}, variety={})>"\
                .format(self.title, self.author, self.pages, self.published)