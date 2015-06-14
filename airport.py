from json import dump
from selenium import webdriver
import time
import re

class theAddress():
	name = ""
	latitude = ""
	longitude = ""
	city = ""
	address = ""
	country = ""

dumped_results = []

driver = webdriver.Firefox()
driver.get("http://www.prokerala.com/travel/airports/india/")

assert "Airasdfafports" not in driver.title
print "assertion done------> \n"
elem = driver.find_elements_by_css_selector('a[href$="airport.html"]')
count = 0
for i in range(count, len(elem)):
	elem = driver.find_elements_by_css_selector('a[href$="airport.html"]')
	print "Name : %s" % elem[i].text
	name_airport = elem[i].text
	elem[i].click()
	
	lat = driver.find_element_by_xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[1]').text
	lng = driver.find_element_by_xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]').text
	city = driver.find_element_by_xpath('//*[@id="body"]/div[2]/table/tbody/tr[3]/td[1]').text
	country = "INDIA"
	address = driver.find_element_by_xpath('//*[@id="body"]/div[2]/table/tbody/tr[5]/td').text
	plat = re.findall('(?<=Latitude : ).+',lat)
	plng = re.findall('(?<=Longitude : ).+',lng)
	pcity = re.findall('(?<=City : ).+',city)
	paddress = re.findall('(?<=:).+(?=,India|, India)',address)
	
	obj = theAddress()
	obj.name = name_airport
	obj.latitude = plat
	obj.longitude = plng
	obj.city = pcity
	obj.country = "India"
	try:
		obj.address = paddress[0] + ", India."
	except IndexError:
		obj.address = address + ", India."
	print "%s" % plat[0]
	print "%s" % plng[0]
	print "%s" % pcity[0]
	try:
		print "%s" % paddress[0]
	except IndexError:
		paddress = address
		print paddress

	dumped_results.append(obj.__dict__)

	driver.back()

	with open('airports_addr.json','w') as filer:
		dump(dumped_results, filer, indent = 1)


	

	#//*[@id="body"]/div[2]/table/tbody/tr[2]/td[1]
	#//*[@id="body"]/div[2]/table/tbody/tr[2]/td[1]