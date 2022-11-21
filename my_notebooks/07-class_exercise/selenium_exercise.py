import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

import bs4


import bs4
import json
'''Use selenium to go to amazon.com and search for Pet Shower Cap - Waterproof Reusable Bath Ear Covers
Print how many products were found
Find the cheapest and the most expensive product from the list'''

base_url = 'http://www.amazon.com'
options = Options()
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options) # or use driver = webdriver.PhantomJS() which will do the same without the overhead of a GUI. http://phantomjs.org/download.html

browser.get(base_url)

search_field = browser.find_element(By.ID, "twotabsearchtextbox")
search_text = "Pet Shower Cap"
search_field.send_keys(search_text)
search_field.submit()
time.sleep(1)
soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
# Get result count:
result_count = soup.select('div[id=search] > span[class=rush-component] > div > h1 > div > div > div > div > span')[0].text[8:11]
print(f"Amount of results for '{search_text}': {result_count}")


time.sleep(1)
# Get Cheapest :
# 1) Get page by showing a Lowest To Highest price page
sort_button = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span/span")
sort_button.click()
time.sleep(1)

sort_button = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/ul/li[2]')
sort_button.click()
time.sleep(1)

# 2) Get first item on page, and it's price
dollar = browser.find_element(By.CSS_SELECTOR, '.widgetId\=search-results_1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(2) > span:nth-child(2)').text
time.sleep(1)

cents = browser.find_element(By.CSS_SELECTOR, '.widgetId\=search-results_1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(2) > span:nth-child(3)').text
time.sleep(1)

lowest_price = dollar + "." + cents
print(f"Cheapest '{search_text}' is priced: ${lowest_price}")



