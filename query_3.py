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

query = select([orders.c.id, func.JulianDay(orders.c.Shipping_date) - func.JulianDay(datetime.now())]) \
    .select_from(orders)

result = connection.execute(query).fetchall()

# for r,c in result:
#     print(r,c)

for r, c in result:
    # print(c)
    if c >= 5:
        print(r, "Processing")
    if 3 <= c < 5:
        print(r, "Packing")
    if 1 <= c < 3:
        print(r, "Shipping")
    if c < 1:
        print(r, "Delivered")
