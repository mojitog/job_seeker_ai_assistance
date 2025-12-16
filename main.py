import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://recruitment.uni.lu/en/index.html?LOV52=11696&SUBDEPT2=All&LOV53=All&keywords=&Resultsperpage=50&srcsubmit=Search&statlog=1&ID=QMUFK026203F3VBQB7V7VV4S8&mask=karriereseiten&LG=UK"
page = requests.get(url)


options = Options()
#options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get(url)
driver.implicitly_wait(5)

#expertise_selector = driver.find_element(By.ID, "ConfLov_11694")
expertise_selector = driver.find_element(By.CSS_SELECTOR, "#ConfLov_11694")
#print(expertise_selector.id)
expertise_dropdown = Select(expertise_selector)
expertise_dropdown.select_by_visible_text("PhD Candidates")

search_button = driver.find_element(By.CSS_SELECTOR, "#srcsubmit")
search_button.click()

job_ads = driver.find_elements(By.CSS_SELECTOR, "table.Lst-Tabel tbody > tr > td > a")
for job in job_ads:
    print(job.text, job.get_attribute("href"))
    #job_page = requests.get(job.get_attribute("href"))
    #soup = BeautifulSoup(job_page.content, "html.parser")


print(len(job_ads))
driver.quit()

#session = HTMLSession()
#r = session.get(url)

with open("output.txt", "w", encoding="UTF-8") as file:
    file.write(page.text)