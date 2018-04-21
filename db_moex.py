from core import flask_app, db

class Stock(db.Model):
    __tablename__ = 'stock_ticker'
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(5), unique=True)
    stock_price = db.relationship('Prise', backref='stocks')

    def __init__(self, stock_name=None):
        self.stock_name = stock_name

    def __repr__(self):
        return '<Stock {} >'.format(self.stock_name)


class Prise(db.Model):
    __tablename__ = 'stock_price'
    id = db.Column(db.Integer, primary_key=True)
    tradedate = db.Column(db.DateTime)
    secid = db.Column(db.String(5))
    value = db.Column(db.Integer)
    opens = db.Column(db.Integer)
    low = db.Column(db.Integer)
    high = db.Column(db.Integer)
    close = db.Column(db.Integer)
    stock_ticker_id = db.Column(db.Integer, db.ForeignKey('stock_ticker.id'))

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
    with flask_app.app_context():
        db.create_all()