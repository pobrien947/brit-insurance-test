from sqlalchemy import Column, DateTime, BigInteger, Float, Integer, Index, Boolean, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base(name='Model')


class User(Model):
    """
    SQLAlchemy User model
    """
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    auth_token = Column(String(255), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
