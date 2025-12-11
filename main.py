import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#from requests_html import HTMLSession
#from bs4 import beautifulsoup

url = "https://recruitment.uni.lu/en/index.html?LOV52=11696&SUBDEPT2=All&LOV53=All&keywords=&Resultsperpage=50&srcsubmit=Search&statlog=1&ID=QMUFK026203F3VBQB7V7VV4S8&mask=karriereseiten&LG=UK"
page = requests.get(url)


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get(url)
print(driver.title)
driver.quit()

#session = HTMLSession()
#r = session.get(url)

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(page.text)