import re
import urllib.request, urllib.parse, urllib.error
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import ssl
import csv

def enter_destination(link, prime) :
	url = link
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	mod = hunt(soup, prime, link)
	return mod

def hunt(soup, prime, link) :
	tr_tags = list()
	keylist = list()
	valuelist = list()
	table_tags = list()
	return_list = list()
	sorted_keys = list()
	sorted_values = list()
	div_tags = soup.find_all('div', id='scrollDiv')

	for d in div_tags :
		table_tags = d.find_all('table')
		for i in range(len(table_tags)) :
			tr_tags.extend(table_tags[i].find_all('tr'))
		for i in range(len(tr_tags)) :
			keylist.append(tr_tags[i].find('td').text)
			valuelist.append(tr_tags[i].find('td').findNext('td').span.text)

	Company = re.findall('trucks/(.+?)/', line)
	Model = re.findall('https://trucks.cardekho.com/en/trucks/.+/(.+?)/specifications', line)
	keylist.append("Company")
	keylist.append("Model")
	valuelist.append(Company)
	valuelist.append(Model)
	for x in prime :
		if x not in keylist :
			keylist.append(x)
			valuelist.append('')

	dictionary = dict(zip(keylist, valuelist))
	for key in sorted(dictionary.keys()) :
		sorted_keys.append(key)
		sorted_values.append(dictionary[key])
	print(len(dictionary))
#	print(keylist)
	
	return sorted_values
		

#def mega_kill() :
#	fh = open("Tata ACE Specifications & Features - TrucksDekho.html")
#	soup = BeautifulSoup(fh, 'html.parser')
#	hunt(soup)

#def merge(dict1, dict2) :
#	return(dict2.update(dict1))

#mega_kill()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

master = list()
count = 0
prime = ['Max Power', 'Displacement (cc)', 'Transmission', 'Gearbox', 'Clutch', 'Fuel Type', 'Emission Norms', 'Engine', 'Engine Displacement', 'Max Torque', 'GVW / GCW (Kgs)', 'Wheelbase (mm)', 'Number of Tyre', 'Chassis Type', 'Cabin Type', 'Body Option', 'Front Tyre', 'Kerb Weight (Kgs)', 'Rear Tyre', 'A/C', 'Seat Type', 'Steering', 'Driver Information Display', 'Adjustable Driver Seat', 'Seating Capacity', 'Rear Suspension', 'Power Steering', 'Parking Brakes', 'Seat Belts', 'Brakes', 'Front Suspension', 'Chassis', 'Electricals', 'Height {mm (ft.)}', 'Fuel Tank (Litres)', 'Max Speed (km/h)', 'Gradeability (%)', 'Turning Radius (mm)', 'Engine Cylinders', 'Payload (Kgs)', 'Tiltable Cabin', 'Ground Clearance (mm)', 'Overall Height (mm)', 'Axle Configuration', 'Overall Length (mm)', 'Overall Width (mm)', 'Cruise Control', 'Navigation System', 'Telematics', 'Arm-rest', 'Tiltable Steering', 'ABS', 'Hill Hold', 'Fog Lights', 'Tubeless Tyres', 'Rear Axle', 'Front Axle', 'Width {mm (ft.)}', 'Mileage', 'Length {mm (ft.)}', 'Bulker Electricals', 'Floor Material', 'Side Board Material', 'Rear Board Material', 'External/Interior Surface', 'Axle Types', 'Refrigerating Unit', 'Body Brakes', 'Temperature Range', 'No. Of Axles', 'Landing Gear', 'Bulker Pressure', 'Floor Type', 'Size (Cu. M)', 'Body Material', 'Canopy Length', 'Water Tank Capacity (KL)', 'Water Tank Type', 'No. Of Valves', 'Pump Type', 'Bulker Type', 'Bulker Discharge Pipe', 'Bulker Air Inlet Pipe', 'Bulker Equipments', 'Battery(Volts)', 'Loading Platform Area(Sq.ft)', 'Alternator (Amps)']
#prime =['Max Power', 'Displacement (cc)', 'Fuel Tank (Litres)', 'Transmission', 'Emission Norms', 'Engine', 'Max Torque', 'Turning Radius (mm)', 'Engine Cylinders', 'Gearbox', 'Clutch', 'Gradeability (%)', 'Fuel Type', 'GVW / GCW (Kgs)', 'Wheelbase (mm)', 'Payload (Kgs)', 'Front Tyre', 'Rear Tyre', 'Overall Length (mm)', 'Kerb Weight (Kgs)', 'Overall Height (mm)', 'Number of Tyre', 'Chassis Type', 'Cabin Type', 'Body Option', 'Ground Clearance (mm)', 'Overall Width (mm)', 'A/C', 'Seat Type', 'Steering', 'Driver Information Display', 'Adjustable Driver Seat', 'Tiltable Steering', 'Seating Capacity', 'Parking Brakes', 'Seat Belts', 'Brakes', 'Power Steering', 'Front Suspension', 'Rear Suspension', 'Chassis', 'Length {mm (ft.)}', 'Width {mm (ft.)}', 'Max Speed (km/h)', 'Axle Configuration', 'Tiltable Cabin', 'Cruise Control', 'Navigation System', 'Telematics', 'Arm-rest', 'Tubeless Tyres', 'Hill Hold', 'Rear Axle', 'Front Axle', 'ABS', 'Fog Lights', 'Canopy Length', 'Water Tank Capacity (KL)', 'Battery(Volts)', 'Water Tank Type', 'No. Of Valves', 'Pump Type', 'Bulker Type', 'Bulker Discharge Pipe', 'Bulker Air Inlet Pipe', 'Bulker Equipments', 'Bulker Electricals', 'Floor Material', 'Side Board Material', 'Rear Board Material', 'External/Interior Surface', 'Size (Cu. M)', 'Refrigerating Unit', 'No. Of Axles', 'Temperature Range', 'Electricals', 'Landing Gear', 'Body Brakes', 'Floor Type', 'Height {mm (ft.)}', 'Body Material']
#master.append(prime.sort())

fh = open('links.csv')
for line in fh :
	if count > 0 :
		line = line.strip()
		print(line)
		master.append(enter_destination(line, prime))
		prime = enter_destination(line, prime)
		print(count)
	count += 1
	if count == 5:
		break
#print(len(prime))
print(sorted(prime))
data = pd.DataFrame(master)
data.to_csv('Truck_Master.csv')
#heads = pd.DataFrame(sorted(prime))
#sorted(prime).to_csv('Heads.csv')
#print(data)

#link = "https://trucks.cardekho.com/en/trucks/eicher/pro-1110-xp/specifications"
#enter_destination(link, prime)
