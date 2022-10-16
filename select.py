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

actor = s.Table('actor', metadata, autoload=True, autoload_with=engine)
film = s.Table('film', metadata, autoload=True, autoload_with=engine)

# query
select_query = s.select([actor])

film_query = s.select([film])

# execute query

result_proxy1 = connection.execute(select_query)
result_proxy2 = connection.execute(film_query)

fetch1 = result_proxy1.fetchmany(5)
fetch2 = result_proxy2.fetchmany(5)

pprint(fetch1)

print("\n**************************************** \n")

