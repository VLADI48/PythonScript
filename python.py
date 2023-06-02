#!/usr/bin/env python3
#Developed by Bogatov Vladimir Vladimirovich

import pandas as pd

import MySQLdb


#Connection to the database
conn = MySQLdb.connect("YourHost", "YourUser", "YourPassword", "YourDataBase")


#Open and write to a file
f = open('/var/www/html/python.html','w')

message = """

<!DOCTYPE html>

<html>

<head>

  <title>python</title>

  <meta charset="utf-8" />

  <style>

    table {

      width: 55%;

      border-collapse: collapse;

    }

    caption {

      text-align: center;

      color: #000000;

      font-weight: bold;

    }

    td, th {

      border: 1px solid #98bf21;

      padding: 3px 7px 2px 7px;

    }

    th {

      text-align: left;

      padding: 5px;

      background-color: #A7C942;

      color: #fff;

    }

    tr:hover { background-color: #EAF2D3; }

  </style>

</head>

<body><p>Hello python!</p>

"""

f.write(message)

f.close()



cursor = conn.cursor()

cursor.execute("SELECT * FROM articles")

f = open('/var/www/html/python.html','a')

message = "<table><caption>Вывод данных из таблицы articles</caption><tr><th>id</th><th>magazines_id</th><th>article_type_id</th><th>author_id</th></tr>"

f.write(message)

f.close()

for row in cursor.fetchall():

	with open('/var/www/html/python.html','a') as f:

        	print('<tr><td>', row[0], '</td>', '<td>', row[1], '<td>', row[2], '</td>', '<td>', row[3], '</td></tr>', file=f)

cursor.close()

f = open('/var/www/html/python.html','a')

message = "</table><br></br>"

f.write(message)



cursor = conn.cursor()

cursor.execute("SELECT * FROM author")

f = open('/var/www/html/python.html','a')

message = "<table><caption>Вывод данных из таблицы author</caption><tr><th>id</th><th>author</th></tr>"

f.write(message)

f.close()

for row in cursor.fetchall():

        with open('/var/www/html/python.html','a') as f:

                print('<tr><td>', row[0], '</td>', '<td>', row[1], '</td></tr>', file=f)

cursor.close()

f = open('/var/www/html/python.html','a')

message = "</table><br></br>"

f.write(message)



cursor = conn.cursor()

cursor.execute("SELECT * FROM article_types")

f = open('/var/www/html/python.html','a')

message = "<table><caption>Вывод данных из таблицы article_types</caption><tr><th>id</th><th>type</th></tr>"

f.write(message)

f.close()

for row in cursor.fetchall():

        with open('/var/www/html/python.html','a') as f:

                print('<tr><td>', row[0], '</td>', '<td>', row[1], '</td></tr>', file=f)

cursor.close()

f = open('/var/www/html/python.html','a')

message = "</table><br></br>"

f.write(message)



cursor = conn.cursor()

cursor.execute("SELECT * FROM article_types")

f = open('/var/www/html/python.html','a')

message = "<table><caption>Вывод данных из таблицы magazines</caption><tr><th>id</th><th>name</th></tr>"

f.write(message)

f.close()

for row in cursor.fetchall():

        with open('/var/www/html/python.html','a') as f:

                print('<tr><td>', row[0], '</td>', '<td>', row[1], '</td></tr>', file=f)

cursor.close()

f = open('/var/www/html/python.html','a')

message = "</table><br></br></body></html>"

f.write(message)