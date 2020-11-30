import sqlite3

conn = sqlite3.connect("demo.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE report (
    id integer PRIMARY KEY,
    date text NOT NULL,
    recipe_cod text NOT NULL,
    recipe_name text NOT NULL,
    solid text NOT NULL,
    liquid1 text NOT NULL,
    liquid2 text NOT NULL,
    powder text NOT NULL,
    blend_time integer NOT NULL
)"""
cursor.execute(sql_query)

sql_query = """ CREATE TABLE recipe (
    id integer PRIMARY KEY,
    recipe_cod text NOT NULL,
    recipe_name text NOT NULL,
    solid text NOT NULL,
    liquid1 text NOT NULL,
    liquid2 text NOT NULL,
    powder text NOT NULL,
    blend_time integer NOT NULL
)"""
cursor.execute(sql_query)