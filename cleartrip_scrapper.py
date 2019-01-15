import os 
import re
import sys
import time
import json
import urllib
import urllib.request
from urllib import parse
from random import randint
from selenium import webdriver
from urllib.parse import urlparse
from selenium.common import exceptions  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from google_images_download import google_images_download 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException




entry_URL = 'https://www.cleartrip.com/hotels'

places = open('places.txt','r',encoding='utf-8')

# Taking Control of the browser ....
browser = None
try:
    browser = webdriver.Chrome()
except Exception as error:
    print(error)

if browser is None:
    print("Selenium not opened")
    sys.exit()



# Openening hotels page and entering the details ......
for place in places :
    try:
        browser.get(entry_URL)
        time.sleep(5)
        


    except Exception as err:
        print(str(err))
        break 
    else:
        print('Working on :', place)
    body = browser.find_element_by_tag_name('body')
    input_box = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="text"][@placeholder="Enter Locality, Landmark, City or Hotel"]')))
    input_box.clear()
    for char in place :
        time.sleep(0.1)
        input_box.send_keys(char)
        time.sleep(0.8)
    time.sleep(5)
    body.send_keys(Keys.ENTER)
    time.sleep(5)
    check_in_element = browser.find_element_by_xpath('//input[@type="text"][@title="Check-in date"]')
    
    time.sleep(2)
    check_in_element.send_keys(Keys.ENTER)
    time.sleep(1)
    check_out_element = browser.find_element_by_xpath('//input[@type="text"][@title="Check-out date"]')
    
    time.sleep(2)
    check_out_element.send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_tag_name('body').click()
    search_hotels_btn =  WebDriverWait(browser, 120 ,ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,))\
                        .until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"][@id="SearchHotelsButton"]')))
    browser.execute_script("arguments[0].click();",search_hotels_btn)
    time.sleep(1)
    # Insert your code below ....... 
