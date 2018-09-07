from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time,random
from selenium.webdriver.chrome.options import Options
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')


prefs = {"profile.default_content_setting_values.notifications" : 2,"profile.managed_default_content_settings.images":2,"network.cookie.cookieBehavior": 2}

chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://e7sc25l8hp1xy8t-anticaptcha.labs.icec.tf/")
total= driver.find_element_by_tag_name("tbody")
k=0
def checkprime(a):
	for i in range(2,a):
		if(a%i==0):
			return False
	return True
def greatest(a,b):
	c=min(a,b)
	for i in range(c,0,-1):
		if(a%i==0 and b%i==0):
			return i
for i in total.find_elements_by_xpath("//tr")[1:]:
    soup=i.text
    if('prime' in soup and 'number' in soup):
    	a=soup.split(' ')
    	if(checkprime(int(a[1]))):
    		i.find_elements_by_xpath('//input')[k].send_keys('true')
    		k=k+1
    	else:
    		i.find_elements_by_xpath('//input')[k].send_keys('false')
    		k=k+1
    elif('divisor' in soup and 'greatest' in soup):
    	a=soup.split(' ')
    	gcd=greatest(int(a[7]),int(a[9].replace('?','')))
    	print(a[8])
    	i.find_elements_by_xpath('//input')[k].send_keys(str(gcd))
    	k=k+1
    elif('following' in soup ):
    	a=soup.split(' ')
    	if('th' in a[3]):
    		number=int(a[3].split('th')[0])
    	elif('st' in a[3]):
    		number=int(a[3].split('st')[0])
    	elif('nd' in a[3]):
    		number=int(a[3].split('nd')[0])
    	elif('rd' in a[3]):
    		number=int(a[3].split('rd')[0])
    	strin=(' '.join(a[9:])).split(' ')
    	i.find_elements_by_xpath('//input')[k].send_keys(str((strin[number-1]).replace('.','')).replace(',',""))
    	k=k+1
    else:
    	k=k+1
    	print(soup)
    #soup=BeautifulSoup(i,'html.parser')
    #texting=soup.find('td')[0].text
    #i.find_element_by_xpath('//td')[1].click()


