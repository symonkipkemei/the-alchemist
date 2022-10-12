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
query = s.update(kipchumba).values(salary=100000)


 # execute query
result = connection.execute(query)

