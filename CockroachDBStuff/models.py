
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import Column, Index, String, DateTime, Integer, Float, \
    PrimaryKeyConstraint, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.types import DECIMAL
from sqlalchemy.dialects.postgresql import UUID, JSONB

import datetime

from generators import BloxGenerator

#@todo: add interleaving
#@todo: restore FKs and "relationship' functionality after this is fixed: https://github.com/cockroachdb/cockroach/issues/36859

#default to the single region schema and dynamically make multi-region based on command line args.

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, default=BloxGenerator.generate_uuid)
    key = Column(String, nullable=False)
    crypto = Column(String)

    Index('userkey', wallet)

    def __repr__(self):
        return "<Key(PrivateKey='%s', id='%s', crypto='%s')>" % (self.key, self.id, self.value)

