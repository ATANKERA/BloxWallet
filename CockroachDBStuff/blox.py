from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction
from generators import BloxGenerator

import datetime, logging

class Blox:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def __init__(self, conn_string, init_tables = False, multi_region = False, echo = False):

        self.keys = env.keys
        self.crypto = create_crypto(conn_string, convert_unicode=True, echo=echo)


        if init_tables:
            logging.info("initializing tables")
            Base.metadata.drop_all(bind=self.engine)
            Base.metadata.create_all(bind=self.engine)


            logging.debug("tables dropped and created")

        self.session = sessionmaker(bind=self.engine)()
