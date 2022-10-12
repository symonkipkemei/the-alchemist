import sqlalchemy as s
import os
import pymysql
from pprint import pprint

password = os.environ["PW_MYSQL_ROOT"]

#connection
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/sakila")
connection = engine.connect()
metadata = s.MetaData()


#create a table objects
actor = s.Table("actor", metadata, autoload=True, autoload_with=engine)
film = s.Table("film", metadata, autoload=True, autoload_with=engine)
film_actor = s.Table("film_actor", metadata, autoload=True, autoload_with=engine)

#pprint(actor.columns.keys())
#pprint(repr(metadata.tables["actor"]))


#the join query
join_statement = actor.join(film_actor,film_actor.columns.actor_id == actor.columns.actor_id).join(film,film.columns.film_id == film_actor.columns.film_id)

join_query = s.select([film.columns.film_id,film.columns.title,actor.columns.first_name,actor.columns.last_name]).select_from(join_statement)

#create a query
actor_query = s.select([actor]).where(actor.columns.first_name.in_(["PENELOPE","PARKER","UMA"]))

film_query = s.select([film]).where(s.and_(film.columns.length > 60,film.columns.rating =="PG"))

query = s.select([film]).where(film.columns.title == "AFRICAN EGG")

film_orderby_query = s.select([film]).order_by(s.asc(film.columns.replacement_cost))

film_length_query = s.select([s.func.sum(film.columns.length)])

search_query = s.select([actor]).where(actor.columns.first_name == 'PENELOPE') 

# execute the query via the connection
result_proxy = connection.execute(query)

# fetch results from executed query
result_set = result_proxy.fetchall()
pprint(result_set)



#USING JOINS


