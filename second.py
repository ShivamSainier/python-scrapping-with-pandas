import requests
import csv

list1=[]
list2=[]
list3=[]

with open('IMAGES.csv','r') as csv_file:
    csv_data=csv.reader(csv_file)
    for rows in csv_data:
        list1.append(rows[1])

del list1[0]
for i in range(len(list1)):
    req=requests.get(list1[i])
    list2.append(req.content)

for i in range(len(list2)):
    j=input("enter name: ")
    k=f"{j}.jpg"
    list3.append(k)

for i in range(len(list3)):
    with open (list3[i],'wb') as app:
        app.write(list2[i])
print("work done")

