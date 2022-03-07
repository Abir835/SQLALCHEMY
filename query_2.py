from operator import add
from unittest import result
from sqlalchemy import between, create_engine, MetaData, Table, Column, Integer, String, ForeignKey, desc, join, Date, \
    and_
from sqlalchemy.sql import select, func
from sqlalchemy.sql.expression import update
from datetime import datetime
from sqlalchemy import column

from main import engine, meta, connection, customers, orders, orders_Items, products

customers = Table('customers', meta, autoload=True, autoload_with=engine)
orders = Table('orders', meta, autoload=True, autoload_with=engine)
products = Table('products', meta, autoload=True, autoload_with=engine)
orders_Items = Table('orders_Items', meta, autoload=True, autoload_with=engine)

query = select(
    [customers.c.name.label('c_name'), products.c.name.label('p_name'), func.sum(orders_Items.c.qty).label('total')]) \
    .select_from(join(customers, orders).join(orders_Items).join(products)) \
    .group_by(customers.c.name, products.c.name) \
    .order_by(customers.c.name)

result = connection.execute(query).fetchall()

for r in result:
    print(r)

query2 = select([query.c.c_name, query.c.p_name, func.max(query.c.total)]) \
    .select_from(query) \
    .group_by(query.c.c_name)

result = connection.execute(query2).fetchall()

for r in result:
    print(r)
