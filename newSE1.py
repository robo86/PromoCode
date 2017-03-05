"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""
import time
import csv
import pyodbc
import os

os.system('cls')

server = 'x'
database = 'x'
username = 'x'
password = 'x'
driver= '{ODBC Driver 13 for SQL Server}'

#set up the lists
alt_list = []
exclude_vendor = ['Specialized','Wahoo Fitness','Keiser','Garmin']
exclude_category =["Bicycle > Accessories >Brands","Bicycle > Accessories > Electronics > Video Cameras","Bicycle > Accessories > Electronics > Cameras","Bicycle > Accessories > Trailers/Strollers > Cargo Trailers","Bicycle > Accessories > Trailers/Strollers > Child Trailers","Bicycle > Accessories > Trailers/Strollers > Strollers/Joggers","Bicycle > Accessories > Trailers/Strollers > Trailer Bikes","Bicycle > Accessories > Trailers/Strollers > Pet Bicycle Carriers","Bicycle > Accessories > Media','esources > Software","Bicycle > Car Racks > Roof Mount Cargo Boxes/ Carriers","Bicycle > Fitness Equipment > Elliptical Machines","Bicycle > Fitness Equipment > Indoor Cycles","Bicycle > Fitness Equipment > Inversion Products","Bicycle > Fitness Equipment > Recumbent Exercise Bikes","Bicycle > Fitness Equipment > Rowers","Bicycle > Fitness Equipment > Treadmills","Bicycle > Fitness Equipment > Upright Exercise Bikes","Bicycle > Fitness Equipment > Steppers","Bicycle > Fitness Equipment > Vertical Knee Raise Machine","Bicycle > Fitness Equipment > Weights","Bicycle > Demo Products > Wheels","Bicycle > Novelties/Gift Ideas > Novelties/ Gift Ideas","Bicycle > Novelties/Gift Ideas > Holiday Gift Ideas","Bicycle >Gift Cards","Bicycle > Bikes > BMX > BMX","Bicycle > Bikes > BMX > Freestyle","Bicycle > Bikes > BMX > Freestyle | Bicycle > Bikes > BMX > Jump","Bicycle > Bikes > Children's > 12-Inch (2-4 yr. old)","Bicycle > Bikes > Children's > 12-Inch (2-4 yr. old) | Bicycle > Bikes > Children's > Running Bikes","Bicycle > Bikes > Children's > 16-Inch (3-6 yr. old)","Bicycle > Bikes > Children's > 16-Inch (3-6 yr. old) | Bicycle > Bikes > BMX > BMX","Bicycle > Bikes > Children's > 16-Inch (3-6 yr. old) | Bicycle > Bikes > BMX > Freestyle","Bicycle > Bikes > Children's > 18-Inch (4-7 yr. old)","Bicycle > Bikes > Children's > 18-Inch (4-7 yr. old) | Bicycle > Bikes > BMX > Freestyle","Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old)","Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old) | Bicycle > Accessories > Trailers/Strollers > Trailer Bikes","Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old) | Bicycle > Bikes > BMX > BMX","Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old) | Bicycle > Bikes > BMX > Freestyle","Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old) | Bicycle > Bikes > BMX > Jump","Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Children's > 24-Inch (7+ yr. old) | Bicycle > Bikes > BMX > Freestyle","Bicycle > Bikes > Children's > Running Bikes","Bicycle > Bikes > Children's > Scooters","Bicycle > Bikes > Children's > Tricycles","Bicycle > Bikes > Comfort","Bicycle > Bikes > Comfort | Bicycle > Bikes > Cruiser","Bicycle > Bikes > Comfort | Bicycle > Bikes > Cruiser | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Comfort | Bicycle > Bikes > Hybrid","Bicycle > Bikes > Comfort | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed","Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed | Bicycle > Bikes > Cruiser","Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed | Bicycle > Bikes > Hybrid | Bicycle > Bikes > Fitness","Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed | Bicycle > Bikes > Road > Track","Bicycle > Bikes > Commuter/Urban > Frames","Bicycle > Bikes > Commuter/Urban > Multi-Speed","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Comfort","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Comfort | Bicycle > Bikes > Cruiser","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Comfort | Bicycle > Bikes > Fitness","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Comfort | Bicycle > Bikes > Hybrid","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Comfort | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Cruiser","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Cruiser | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Fitness","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Hybrid","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Hybrid | Bicycle > Bikes > Fitness","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Hybrid | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Hybrid | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Other > Adult Tricycles","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Other > Electric | Bicycle > Bikes > Other > Adult Tricycles","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Other > Folding | Bicycle > Bikes > Folding","Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Cruiser","Bicycle > Bikes > Cruiser | Bicycle > Bikes > Children's > 16-Inch (3-6 yr. old)","Bicycle > Bikes > Cruiser | Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old)","Bicycle > Bikes > Cruiser | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Cruiser | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Cruiser | Bicycle > Bikes > Other > Tandem > Comfort/Hybrid","Bicycle > Bikes > Cyclocross > Cyclocross Bikes","Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Commuter/Urban > Multi-Speed","Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Cyclocross > Cyclocross Frames","Bicycle > Bikes > Cyclocross > Cyclocross Frames | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Electric Self Balancing Scooters","Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Fitness","Bicycle > Bikes > Folding","Bicycle > Bikes > Hybrid","Bicycle > Bikes > Hybrid | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Hybrid | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old) | Bicycle > Bikes > Fitness","Bicycle > Bikes > Hybrid | Bicycle > Bikes > Fitness","Bicycle > Bikes > Hybrid | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Hybrid | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Mountain > 26-Inch Wheel","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers)","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Unsuspended","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Dirt Jump","Bicycle > Bikes > Mountain > Dirt Jump | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Downhill/Freeride","Bicycle > Bikes > Mountain > Downhill/Freeride | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Downhill/Freeride | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Downhill/Freeride | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Front-Suspension","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old)","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 26-Inch Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 27.5-Inch Plus Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers)","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > 29-Inch Plus Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 29-Inch Plus Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Mountain > Front-Suspension | Bicycle > Bikes > Other > Electric | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 27.5-Inch Plus Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers)","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > Downhill/Freeride | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 27.5-Inch Plus Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Full-Suspension | Bicycle > Bikes > Other > Electric | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Unsuspended","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Children's > 16-Inch (3-6 yr. old)","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old)","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Children's > 20-Inch (5-8 yr. old) | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old) | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Mountain > 26-Inch Wheel","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Cruiser","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Hybrid","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > 27.5-Inch Plus Wheel","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > 650B Wheel","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Commuter/Urban > Frames | Bicycle > Bikes > Mountain > 26-Inch Wheel","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Fat Bikes","Bicycle > Bikes > Mountain > Unsuspended | Bicycle > Bikes > Mountain > Mountain Frames | Bicycle > Bikes > Mountain > 27.5-Inch Plus Wheel","Bicycle > Bikes > Other > Adult Tricycles","Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Other > Electric | Bicycle > Bikes > Other > Adult Tricycles","Bicycle > Bikes > Other > Folding","Bicycle > Bikes > Other > Folding | Bicycle > Bikes > Folding","Bicycle > Bikes > Other > Stationary | Bicycle > Fitness Equipment > Indoor Cycles","Bicycle > Bikes > Other > Stationary | Bicycle > Fitness Equipment > Indoor Cycles | Bicycle > Fitness Equipment > Upright Exercise Bikes","Bicycle > Bikes > Other > Tandem > All-Terrain","Bicycle > Bikes > Other > Tandem > Comfort/Hybrid","Bicycle > Bikes > Other > Tandem > Road","Bicycle > Bikes > Other > Unicycles","Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Road Frames","Bicycle > Bikes > Road > Road Frames | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Road Frames | Bicycle > Bikes > Road > Track","Bicycle > Bikes > Road > Sport/Performance","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Children's > 24-Inch (7+ yr. old)","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Commuter/Urban > Fixed/One-Speed | Bicycle > Bikes > Road > Track","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Fitness","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Hybrid","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Cyclocross > Cyclocross Bikes | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Other > Electric","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Road > Road Frames","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Road > Road Frames | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Sport/Performance | Bicycle > Bikes > Road > Triathlon/Time Trial","Bicycle > Bikes > Road > Touring","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Commuter/Urban > Multi-Speed","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Hybrid | Bicycle > Bikes > Road > Endurance/Gravel | Bicycle > Bikes > Fitness","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers)","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Mountain > 29-Inch Wheel (29ers) | Bicycle > Bikes > Mountain > Unsuspended","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Mountain > Mountain Frames","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Road > Road Frames","Bicycle > Bikes > Road > Touring | Bicycle > Bikes > Road > Road Frames | Bicycle > Bikes > Commuter/Urban > Multi-Speed | Bicycle > Bikes > Road > Endurance/Gravel","Bicycle > Bikes > Road > Track","Bicycle > Bikes > Road > Triathlon/Time Trial","Bicycle > Bikes > Road > Triathlon/Time Trial | Bicycle > Bikes > Road > Road Frames"] 

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

print("Copying googlebase data.")
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
