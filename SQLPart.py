# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:30:58 2017

@author: desk243
"""
import csv
import pyodbc

server = '**********'
database = '**********'
username = '**********'
password = '**********'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()
cursor.execute("select @@VERSION")
row = cursor.fetchone()
if row:
    print (row)

cursor = cnxn.cursor()
cursor.execute("delete reo_current_google_promo")

with open ('c:\python\pf1.csv', 'r') as f:
    reader = csv.reader(f)
    data = next(reader) 
    query = 'insert into REO_Current_google_promo values ({0})'
    query = query.format(','.join('?' * len(data)))
    cursor = cnxn.cursor()
    cursor.execute(query, data)
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

