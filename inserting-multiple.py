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
new_records = [{'id':'2', 'name':'record1', 'salary':80000, 'aactive':False},
               {'id':'3', 'name':'record2', 'salary':70000, 'aactive':True}]

insert_query = s.insert(kipchumba,new_records)


# exute query
result_proxy = connection.execute(insert_query)




