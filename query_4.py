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

query = select([customers.c.name, func.count(orders.c.cus_id).label('number_of_order')])\
    .select_from(join(customers, orders))\
    .where(orders.c.order_date >= '2022-02-13', orders.c.order_date <= '2022-03-7')\
    .group_by(customers.c.name)\
    .order_by(func.count(orders.c.cus_id).desc())

result = connection.execute(query).fetchall()

for r in result:
    print(r)
