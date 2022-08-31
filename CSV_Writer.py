#Import CSV
import csv
#Your List with Dictionaries
Your_List= [
    {"Dictionary": "Dictionary_1", "Value_1": "Value_1_1", "Value_2:": "Value_2_1"},
    {"Dictionary": "Dictionary_2", "Value_1": "Value_1_2","Value_2:": "Value_2_2"},
    {"Dictionary": "Dictionary_3", "Value_1": "Value_1_3","Value_2:": "Value_2_3"}
  ]

#Your Headers
Headers = ["Header_1", "Header_2", "Header_3"]

#Create a new CSV file
with open('Your_New_File.csv', 'w', newline='') as outcsv:
#Writes Headers from Headers List
    writer = csv.DictWriter(outcsv, fieldnames = Headers)
    writer.writeheader()
    #Turn Your_list into a Hasable item
    fieldnames= Your_List[0].keys()
    #Writes Your Dictionaries (Your Data)
    writer = csv.DictWriter(outcsv, fieldnames=fieldnames)
    for row in Your_List:
        writer.writerow(row)



