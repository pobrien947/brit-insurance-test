from sqlalchemy import Column, DateTime, BigInteger, Float, Integer, Index, Boolean, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base(name='Model')


class Item(Model):
    """
    SQLAlchemy Item model
    """
    __tablename__ = 'item'

    id = Column(BigInteger, primary_key=True)
    item_name = Column(String(100), unique=True, nullable=False)
    default_price = Column(BigInteger, unique=False, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.item_name
