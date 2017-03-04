"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""
import time

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
with open('pf1.txt', 'w') as file:
    for x in range(1,num_lines):
        if (myList[x][2]) != 'Specialized' and \
           (myList[x][2]) != 'Wahoo Fitness' and \
           (myList[x][2]) != 'Keiser' and \
           (myList[x][2]) != 'Garmin':
               print(myList[x][11], promocode, sep = '\t', file = file)
#comma delim   #print(myList[x][11], promocode, sep = '', file = file)  
#just print (OG)#print(myList[x][11],'\t'+promocode)
            
print("File ""pft1.txt"" saved in the c:\python directory.")
time.sleep(5)
