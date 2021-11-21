import pandas
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from Cleaning_Data import *

# The overall product should allow the user to insert a txt file of what is basically any information about the paper 
# they are looking for and then get all the papers that site a paper from the list like a map of sorts.

# Functions so far:
    # In Cleaning_Data:
        # clean_authors
        # clean_titles
    # In Learn_Scraping:
        # insert_titles
        # Have a method that read's the browser page and looks for a particular title
        # Click on the correct title 
        # Click on the citations page 
        # Click import all
        # Click csv format


# This bit is using selenium and beautiful soup to interact with the web browser

# firefox_driver_path = '/home/mahia/Projects/Webscrape/geckodriver.exe'

# driver = webdriver.Firefox(())

# driver.get("https://www.scopus.com/search/form.uri?display=basic#basic")



# with open("markup.html","w", encoding="utf-8") as file:
#         file.write(driver.page_source)

#Here we are creating a function that will insert the authors into the search bar
def insert_title():
    cleaned = clean_titles()
    for i in range(len(cleaned)):
            cleaned[i].replace(' “', '')
    print(cleaned)
    return cleaned
insert_title()
