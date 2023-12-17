from sqlalchemy import Column, DateTime, BigInteger, Float, Integer, Index, Boolean, ForeignKey, String
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Database:

    def __init__(self, config):
        self.engine = create_engine(
            f"mysql+pymysql://{config['db_user']}:{config['db_pass']}@{config['db_host']}/{config['db_name']}",
            echo=False
        )
        self.db_session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine)
        )
