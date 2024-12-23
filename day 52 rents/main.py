from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://appbrewery.github.io/Zillow-Clone/"
forms_url = "https://forms.gle/JCf9ZAhPVXf392xm8"

links_ele = []
links = []
prices_ele = []
prices = []
add_ele = []
addresses = []


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url= url)



links_ele = driver.find_elements(By.CLASS_NAME, value= "property-card-link")
prices_ele = driver.find_elements(By.CLASS_NAME, value="PropertyCardWrapper__StyledPriceLine")
add_ele =  driver.find_elements(By.CSS_SELECTOR, value="#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a > address")

for i in links_ele:
    links.append(i.get_attribute("href"))
for i in prices_ele:
    prices.append(i.text[:6])
for i in add_ele:
    addresses.append(i.text)



driver.quit()

for i in range(len(links)):
    driver = webdriver.Chrome(options=options)
    driver.get(url = forms_url)
    time.sleep(3)

    in1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in2 = driver.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')



    in1.send_keys(addresses[i])
    in2.send_keys(prices[i])
    in3.send_keys(links[i])

    submit.click()







