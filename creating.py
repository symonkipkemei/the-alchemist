from email.policy import default
import string
import sqlalchemy as s
import os
import pymysql
from pprint import pprint

password = os.environ["PW_MYSQL_ROOT"]

#connection
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/sakila")

metadata = s.MetaData()

# creating a new table
newtable = s.Table("kipchumbas", metadata,
s.Column("id",s.Integer()),
s.Column("name",s.String(255), nullable=False),
s.Column("salary", s.Float(), default=100.0),
s.Column("aactive",s.Boolean(), default=True))

metadata.create_all(engine)

