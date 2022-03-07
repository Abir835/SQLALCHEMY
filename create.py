from operator import add
from unittest import result
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, join, Date
from sqlalchemy.sql import select, func
from sqlalchemy.sql.expression import update
from datetime import datetime

from main import engine, meta, connection, customers, orders, orders_Items, products

customers = Table('customers', meta, autoload=True, autoload_with=engine)
orders = Table('orders', meta, autoload=True, autoload_with=engine)
products = Table('products', meta, autoload=True, autoload_with=engine)
orders_Items = Table('orders_Items', meta, autoload=True, autoload_with=engine)

connection.execute(customers.insert(), [
    {'name': 'hasan', 'phone': '01623670581'},
    {'name': 'komal', 'phone': '01623670588'},
    {'name': 'abir', 'phone': '01623670589'},
    {'name': 'rifat', 'phone': '01623670510'},
    {'name': 'faruk', 'phone': '01623670511'},
])

connection.execute(products.insert(), [
    {'name': 'apple'},
    {'name': 'orange'},
    {'name': 'potato', },
    {'name': 'onion', },
    {'name': 'Banana'},
])

connection.execute(orders.insert(), [
    {'cus_id': 1, 'order_date': datetime(2022, 2, 10), 'Shipping_date': datetime(2022, 3, 10), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 2, 'order_date': datetime(2022, 2, 11), 'Shipping_date': datetime(2022, 3, 21), 'total': 3,
     'shipping_status': 0},
    {'cus_id': 1, 'order_date': datetime(2022, 2, 13), 'Shipping_date': datetime(2022, 3, 21), 'total': 1,
     'shipping_status': 0},
    {'cus_id': 2, 'order_date': datetime(2022, 2, 14), 'Shipping_date': datetime(2022, 3, 16), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 3, 'order_date': datetime(2022, 2, 15), 'Shipping_date': datetime(2022, 3, 17), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 4, 'order_date': datetime(2022, 2, 16), 'Shipping_date': datetime(2022, 3, 20), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 5, 'order_date': datetime(2022, 2, 17), 'Shipping_date': datetime(2022, 3, 21), 'total': 1,
     'shipping_status': 0},
    {'cus_id': 2, 'order_date': datetime(2022, 2, 18), 'Shipping_date': datetime(2022, 3, 22), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 2, 'order_date': datetime(2022, 2, 19), 'Shipping_date': datetime(2022, 3, 21), 'total': 2,
     'shipping_status': 0},
    {'cus_id': 3, 'order_date': datetime(2022, 2, 20), 'Shipping_date': datetime(2022, 3, 22), 'total': 2,
     'shipping_status': 0},
])

connection.execute(orders_Items.insert(), [
    {'pro_id': 1, 'or_id': 1, 'qty': 2, 'unit_cost': 20, 'total': 40},
    {'pro_id': 1, 'or_id': 2, 'qty': 2, 'unit_cost': 20, 'total': 40},
    {'pro_id': 5, 'or_id': 2, 'qty': 1, 'unit_cost': 5, 'total': 5},
    {'pro_id': 3, 'or_id': 3, 'qty': 1, 'unit_cost': 10, 'total': 10},
    {'pro_id': 5, 'or_id': 4, 'qty': 1, 'unit_cost': 5, 'total': 5},
    {'pro_id': 3, 'or_id': 4, 'qty': 1, 'unit_cost': 10, 'total': 10},
    {'pro_id': 2, 'or_id': 8, 'qty': 2, 'unit_cost': 25, 'total': 50},
    {'pro_id': 2, 'or_id': 9, 'qty': 2, 'unit_cost': 25, 'total': 50},
    {'pro_id': 2, 'or_id': 6, 'qty': 2, 'unit_cost': 11, 'total': 22},
    {'pro_id': 3, 'or_id': 5, 'qty': 2, 'unit_cost': 10, 'total': 20},
    {'pro_id': 3, 'or_id': 10, 'qty': 2, 'unit_cost': 10, 'total': 20},
    {'pro_id': 5, 'or_id': 7, 'qty': 1, 'unit_cost': 5, 'total': 5},
])
