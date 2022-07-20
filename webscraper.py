import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/nix/path/to/webdriver/executable')
url = "https://bear-rsg.github.io/reconnect/"
driver.get(url)
results = []
content = driver.page_source
soup = BeautifulSoup(content)
