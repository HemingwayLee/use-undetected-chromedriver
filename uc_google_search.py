import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc

try:
    options = uc.ChromeOptions()
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    driver = uc.Chrome(options=options)
    time.sleep(15)
    # driver = webdriver.Chrome(service=service, options=chrome_options) 
    # search_box = driver.find_element(By.NAME, "q")    
    driver.get("https://www.google.com.tw")
    time.sleep(3)

    # search_box = driver.find_element(By.TAG_NAME, "textarea")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("hello")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

except:
    print(traceback.format_exc())

driver.quit()

