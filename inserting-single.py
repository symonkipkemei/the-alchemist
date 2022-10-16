from email.policy import default
import string
import sqlalchemy as s
import os
import pymysql
from pprint import pprint

password = os.environ["PW_MYSQL_ROOT"]

#connection
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/sakila")
connection = engine.connect()
metadata = s.MetaData()


# create a table object

kipchumba = s.Table('kipchumba', metadata, autoload=True, autoload_with=engine)


# create a query
insert_query = s.insert(kipchumba).values(id=1, name ="vincent", salary=60000, aactive=True)


# exute query
result_proxy = connection.execute(insert_query)


