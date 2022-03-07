import sqlalchemy as db
from operator import add
from unittest import result
from sqlalchemy import engine, create_engine, MetaData, Table, Column, String, ForeignKey, Date, join, Integer
from sqlalchemy.sql import func, select
from sqlalchemy.sql.expression import update
from datetime import date

engine = create_engine('sqlite:///customer.db', echo=True)
meta = MetaData()

customers = Table(
    'customers', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('phone', String),
)
orders = Table(
    'orders', meta,
    Column('id', Integer, primary_key=True),
    Column('cus_id', Integer, ForeignKey('customers.id')),
    Column('order_date', db.DateTime),
    Column('Shipping_date', db.DateTime),
    Column('total', Integer),
    Column('shipping_status', Integer),
)

products = Table(
    'products', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

orders_Items = Table(
    'orders_Items', meta,
    Column('id', Integer, primary_key=True),
    Column('pro_id', Integer, ForeignKey('products.id')),
    Column('or_id', Integer, ForeignKey('orders.id')),
    Column('qty', Integer),
    Column('unit_cost', Integer),
    Column('total', Integer),
)

meta.create_all(engine)

connection = engine.connect()
