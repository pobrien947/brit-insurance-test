from sqlalchemy import Column, DateTime, BigInteger, Float, Integer, Index, Boolean, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base(name='Model')


class Basket(Model):
    """
    SQLAlchemy Basket model

    TODO: Although this is called Basket it's really
          the Items within a user's basket.
          Perhaps a rename and refactor of this
    """
    __tablename__ = 'basket'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, unique=False, nullable=False)
    item_name = Column(String(100), unique=True, nullable=False)
    price = Column(BigInteger, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
