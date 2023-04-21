"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12s0r3cv203bug32q0-a.oregon-postgres.render.com",
        database="todo_xnjc",
        user="todo_xnjc_user",
        password="wdu6dsHha8v06L8JYJX0228HYYC3Mvs7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
