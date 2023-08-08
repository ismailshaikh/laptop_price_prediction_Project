# Library Loaded
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Driver Selected
driver = webdriver.Chrome(executable_path="C:/Users/SHAIKH/Desktop/selenium/chromedriver.exe",options=options)

# Navigation
driver.get("https://www.smartprix.com/laptops")

time.sleep(2)

# Page Height
old_height = driver.execute_script('return document.body.scrollHeight')
time.sleep(1)

while True:
    
    # Clicking on Load more
    driver.find_element_by_xpath("//div[@class='sm-load-more']").click()
    time.sleep(2)
    
    # New page geight
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    print(old_height)
    print(new_height)
    
    # checking for page end to end loop
    if new_height == old_height:
        break
    old_height = new_height

# page source store in html
html = driver.page_source

# Create HTML File to scrap data in offline
with open("smartprix_laptop.html", 'w', encoding='utf-8') as f:
    f.write(html)
# 1st stop 279252 height we reach there is unknown error at the end in the main website i think they have not handle the error for no data ahead
# 2nd stop 279342 -> Unknown error, kindly try again
# Finallly hight is 279342 pixels