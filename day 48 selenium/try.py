from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.amazon.in/Creality-Ender-V3-SE-3D/dp/B0CH4MX3S1/ref=sr_1_3?crid=NGW7YWE2ZC1O&dib=eyJ2IjoiMSJ9.i6DI3p_-pvg8cC1goQBI4ciM-xnrWSHcEsr3Hbn5Z_pIdfwZqgwnm-jEpR9sZSbNP17OOomPqVV815nqoe0goMzoNWOoJ6dfdNb5p0POWb-RpYx2_Bmiz75gz_qWNonlyazf8E4k8OjC4lBtr1LlTHXGB8L_tLZfP0Nn9fcnCOTjk4xj2ha2QfCyliwA8chQUZiBMAUmjhOrNmwJ5rb9o5baxoiqjIgZDRljfZ_vxPwvdzgEM2P3qI4uxGq4Tj-0eo6USply6R7NU8b9Y2jEndydxAt2FEek3F6qhIrLirM.SJO_9n0GYWNxTIQmesgYa1cHK5pNA4EGzsKpzJNfa9Y&dib_tag=se&keywords=3d%2Bprinter%2Bcreality%2Bv3&nsdOptOutParam=true&qid=1732101467&sprefix=3d%2Bprinter%2Bcreality%2Bv3%2Caps%2C260&sr=8-3&th=1"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(url)

price_str = driver.find_element(By.CLASS_NAME, value="a-price-whole").text

print(f"The price is {price_str}")

driver.quit()