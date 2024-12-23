from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://orteil.dashnet.org/cookieclicker/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(5)

lang = driver.find_element(By.ID, value="langSelect-EN")
lang.click()

time.sleep(5)
cookie = driver.find_element(By.ID, value="bigCookie")
cookie1 = driver.find_element(By.ID, value="bigCookie")
cookie2 = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie.click()
