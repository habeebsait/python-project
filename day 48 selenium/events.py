from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(url)

time_ = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
event_ = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

dict = {}

for i in range(len(time_)):
    dict.update({i: {"time":time_[i].text, "event":event_[i].text}})

print(dict)


driver.quit()