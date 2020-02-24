import requests
import csv

# empty list
list1=[]
list2=[]
list3=[]

# read "IMAGE.csv" file from current directory
with open('IMAGES.csv','r') as csv_file:
    csv_data=csv.reader(csv_file)
    for rows in csv_data:
        list1.append(rows[1])

# delete the first element from list1 [ which is "0" ]
del list1[0]

# get image data and add into list2
for i in range(len(list1)):
    req=requests.get(list1[i]) 
    list2.append(req.content) 
    k=f"{i}.jpg"           # name of images
    list3.append(k)    # add name of images in list3

#  operation for writing images into current directory 
    with open (list3[i],'wb') as app:
        app.write(list2[i])

print("work done")

