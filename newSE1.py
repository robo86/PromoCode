"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""
import time
import csv
import pyodbc
import os
import categories

os.system('cls')

server = 'server'
database = 'brandscycle'
username = 'sa'
password = 'brands6100'
driver= '{ODBC Driver 13 for SQL Server}'

#set up the lists
alt_list = []
exclude_vendor = ['Specialized','Wahoo Fitness','Keiser','Garmin']
exclude_category = categories.exclude_category

print("The brands to be excluded are:\n "), print(exclude_vendor[0:],"\n")
choice1 = input("Would you like to change the brands (y/n)?: ")
print()
choice1 =choice1.lower()
if choice1 == 'y':
    print("Type brand names one at a time and press ENTER. \nLeave blank and press ENTER when done: ")
    while True:
        alt_vend = input("Brand Name: ")
        if alt_vend == "":
            break
        alt_list.append(alt_vend)
    exclude_vendor = alt_list
os.system('cls')
print('The following brands will be excluded: \n'), print(exclude_vendor)

while True:
    choice2 = input("\n\nWhich file?\n(a if you want to use default categories.  b if you downloaded a new file) \n\na) google_products_file.txt \nb) google_products_file-1.txt \n\n(type a or b): ")
    if choice2 == 'a':
        main_file = 'm:\clothingimport\google_products_file.txt'
        exclude_category =[]
        break
    elif choice2 == 'b':
        main_file = 'm:\clothingimport\google_products_file-1.txt'
        break

promocode = input("\n\nEnter New Promocode: ")

print("\nCopying googlebase data.")
#opens and reads files into variable 'data'
prod = open(main_file, 'r')
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
        if (myList[x][2]) not in exclude_vendor and \
           (myList[x][6]) not in exclude_category:
              print(myList[x][11], promocode, sep = ',', file = file1)  #comma delim
              
#just print (OG)#print(myList[x][11],'\t'+promocode)
#tab delimited print(myList[x][11], promocode, sep = '\t', file = file1)            

#print("File ""pft1.txt"" saved in the c:\python directory.")
print('Done.\n')
#os.system('cls')
print('Emptying table "REO_Current_Google_Promo_Code"')
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

#this is how you run a sql statement - in this case a delete statement
cursor = cnxn.cursor()
cursor.execute("delete reo_current_google_promo")

print('Done\n')
#os.system('cls')
print('Updating Table "REO_Current_Google_Promo_Code"')

#this loops through the csv file created above and inserts each line into the REO... table 

with open ('c:\python\pf1.csv', 'r') as f:
    #x=1
    reader = csv.reader(f)
    data = next(reader) 
    query = 'insert into REO_Current_Google_Promo values ({0})'
    query = query.format(','.join('?' * len(data)))
    cursor = cnxn.cursor()
    cursor.execute(query, data)
    for data in reader:
        cursor.execute(query, data)
        #x=x+1
        #print(x)
        #os.system('cls')
    cursor.commit()

print('All Done')

time.sleep(3)