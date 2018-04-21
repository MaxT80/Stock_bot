from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///moex_base.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Stock(Base):
    __tablename__ = 'stock_ticker'
    id = Column(Integer, primary_key=True)
    stock_name = Column(String(5), unique=True)
    stock_price = relationship('Prise', backref='stocks')

    def __init__(self, stock_name=None):
        self.stock_name = stock_name

    def __repr__(self):
        return '<Stock {} >'.format(self.stock_name)


class Prise(Base):
    __tablename__ = 'stock_price'
    id = Column(Integer, primary_key=True)
    tradedate = Column(DateTime)
    secid = Column(String(5))
    value = Column(Integer)
    opens = Column(Integer)
    low = Column(Integer)
    high = Column(Integer)
    close = Column(Integer)
    stock_ticker_id = Column(Integer, ForeignKey('stock_ticker.id'))

    def __init__(self, tradedate=None, secid=None, value=None,
                 opens=None, low=None, high=None, close=None, stock_ticker_id=None):
        self.tradedate = tradedate
        self.secid = secid
        self.value = value
        self.opens = opens
        self.low = low
        self.high = high
        self.close = close
        self.stock_ticker_id = stock_ticker_id

    def __repr__(self):
        return '<Prise {} {} {} {} {} {} {}>'.format(self.tradedate, self.secid, self.value,
                                                     self.opens, self.low, self.high, self.close)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)