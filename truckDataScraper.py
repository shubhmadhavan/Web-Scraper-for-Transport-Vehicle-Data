import requests
from requests import get
from bs4 import BeautifulSoup
import codecs
import pandas as pd
import numpy as np
import re


soup = BeautifulSoup(open(r"/home/shubh/Desktop/0000 PS1/TrucksInIndia.html"), "html.parser")

#print(soup.prettify())

model=[]
power =[]
gvw =[]
wheelbase =[]
engine =[]
fueltank =[]
payload =[]
imageanddetails =[]

trucks_div=soup.find_all('div', class_="gsc_col-sm-12 gsc_col-md-12 holder")

for container in trucks_div:

    name= container.h3.a.text
    model.append(name)

    truckpower= container.ul.li.find('span',class_='keyValue').text
    power.append(truckpower)

    truckGVW= container.ul.find_all('li',class_='gsc_col-xs-4')[1].text
    gvw.append(truckGVW)


    span_1=container.ul.find_all("span")
    strspan=str(span_1)
    s=strspan[1:-1]

    list_span=s.split(',')
    newlist = [x[:-7] for x in list_span]

    newlist2=[]
    for y in newlist:
        k=re.sub(r'^.*?>', '', y)
        newlist2.append(k)

    keylist=[]
    valuelist=[]
    count=2
    for i in newlist2:
        if count%2==0:
            keylist.append(i)
        else:
            valuelist.append(i)
        count+=1
    dictionary = dict(zip(keylist, valuelist))

    if 'Wheelbase' in dictionary:
        wheelbase.append(dictionary['Wheelbase'])
    else:
        wheelbase.append('')

    if 'Engine' in dictionary:
        engine.append(dictionary['Engine'])
    else:
        engine.append('')

    if 'Fuel Tank' in dictionary:
        fueltank.append(dictionary['Fuel Tank'])
    else:
        fueltank.append('')

    if 'Payload' in dictionary:
        payload.append(dictionary['Payload'])
    else:
        payload.append('')



    imglink= container.h3.a['href']
    imageanddetails.append(imglink)



truckdf = pd.DataFrame({'Model':model,
'Power':power,
'GVW':gvw,
'Payload':payload,
'Fueltank':fueltank,
'Engine':engine,
'WheelBase':wheelbase,
'Image & Other Details':imageanddetails,

})

#print(truckdf)


truckdf.to_csv('CarDekhoScrapedNewTrucks.csv')






