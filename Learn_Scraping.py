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
        # insert_authors
        # Have a method that read's the browser page and looks for a particular title
        # Click on the correct title 
        # Click on the citations page 
        # Click import all
        # Click csv format


# This bit is using selenium and beautiful soup to interact with the web browser (the lines with --->)

#---> firefox_driver_path = '/home/mahia/Projects/Webscrape/geckodriver.exe'

#--->  driver = webdriver.Firefox(())

#---> driver.get("https://www.scopus.com/freelookup/form/author.uri?zone=TopNavBar&origin=NO%20ORIGIN%20DEFINED")



#---> with open("markup.html","w", encoding="utf-8") as file:
#--->         file.write(driver.page_source)

#Here we are creating a function that will insert the authors into the search bar
def insert_author():
    cleaned = clean_author()
    first_name = []
    last_name = []
    for i in range(len(cleaned)):
        if i % 2 == 0:
            first_name.append(cleaned[i])
        else:
            last_name.append(clean_author()[i])

    print(first_name)
insert_author()

