"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""
import time
import csv
import pyodbc

server = 'x'
database = 'x'
username = 'x'
password = 'x'
driver= '{ODBC Driver 13 for SQL Server}'

exclude_vendor = ['Specialized','Wahoo Fitness','Keiser','Garmin']

promocode = input("Enter Promocode: ")

#opens and reads files into variable 'data'
prod = open('m:\clothingimport\google_products_file-1.txt', 'r')
data = prod.read()
prod.close()

#cleans out the nulls (\x00) which cause problems later 
mynew = open('mynew.txt', 'w')
mynew.write(data.replace('\x00', ''))
mynew.close()

#gives number line count to use later in range
num_lines = sum(1 for line in open('mynew.txt'))

#puts line in myList
with open("mynew.txt") as input:
  myList = [(*(line.strip().split('\t') for line in input))]
  
#prints out and saves to file id (part number) 
#and promocode with tab between them
with open('pf1.csv', 'w') as file1:
    for x in range(1,num_lines):
        if (myList[x][2]) not in exclude_vendor:
              print(myList[x][11], promocode, sep = ',', file = file1)  #comma delim
#just print (OG)#print(myList[x][11],'\t'+promocode)
#tab delimited print(myList[x][11], promocode, sep = '\t', file = file1)            
print("File ""pft1.txt"" saved in the c:\python directory.")

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

#this is how you run a sql statement - in this case a delete statement
cursor = cnxn.cursor()
cursor.execute("delete reo_current_google_promo")

print('SQL Table "REO_Current_Google_Promo" Emptied')

#this loops through the csv file created above and inserts each line into the REO... table 
with open ('c:\python\pf1.csv', 'r') as f:
    reader = csv.reader(f)
    data = next(reader) 
    query = 'insert into REO_Current_Google_Promo values ({0})'
    query = query.format(','.join('?' * len(data)))
    cursor = cnxn.cursor()
    cursor.execute(query, data)
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

print('SQL Table "REO_Current_Google_Promo" Updated')

time.sleep(5)

