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

query = select([customers.c.name.label('c_name'), func.sum(orders_Items.c.total).label('total_spend')]) \
    .select_from(join(customers, orders).join(orders_Items)) \
    .where(between(orders.c.order_date, '2020-02-23', '2022-03-6')) \
    .group_by(customers.c.name) \
    .order_by(func.sum(orders_Items.c.total).desc())
# print(query)
result = connection.execute(query).fetchall()
# print(result)
for total in result:
    print(total)
