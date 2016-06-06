from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import time
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

time.sleep(10)

name = sys.argv[1]
to_send = sys.argv[2]

srch = driver.find_element_by_class_name('input-search')
srch.send_keys(name)
time.sleep(3)

srch.send_keys(Keys.ENTER)
msg = driver.find_elements_by_class_name('input')[1]


for i in range(0,20):
	msg.send_keys(to_send)
	msg.send_keys(Keys.ENTER)