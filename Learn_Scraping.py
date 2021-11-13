import pandas
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup



#firefox_driver_path = '/home/mahia/Projects/Webscrape/geckodriver.exe'


with open("markup.html","w", encoding="utf-8") as file:
        file.write(driver.page_source)

#Here we are creating a function that will insert the authors into the search bar
def insert_author():
    with open("research_docs.txt","r") as files:
        lines = files.readlines()
        print(lines)

