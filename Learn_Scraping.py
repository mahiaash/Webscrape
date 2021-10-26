import pandas
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#https://www.udemy.com/courses/free/?lang=en&sort=popularity

sort_by_type = 'newest'

#firefox_driver_path = '/home/mahia/Projects/Webscrape/geckodriver.exe'

delay = 15

#driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver = webdriver.Firefox(())

driver.get("https://www.udemy.com/courses/free/?lang=en&p=10&sort=newest")

try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'course-list--container--3zXPS')))
except TimeoutException:
    
    print('Loading exceeds delay time')
    
else:
    with open("markup.html","w", encoding="utf-8") as file:
        file.write(driver.page_source)
finally:
    driver.quit()
# for page_number in range(1,12):

#     page_url = f"https://www.udemy.com/courses/free/?lang=en&p={page_number}&sort=newest" 