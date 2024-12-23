from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://en.wikipedia.org/wiki/Main_Page"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, value= "search")
search.send_keys("Python", Keys.ENTER)