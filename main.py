from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
ser = Service("YOUR_PATH") #Example: C:\\Users\ACER\Downloads\chromedriver.exe
browser = webdriver.Chrome(service=ser , options=option)

browser.get("http://1.1.1.2/")

try:
    name = browser.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/form/div[1]/input")
    password = browser.find_elements(by=By.XPATH,value="/html/body/div[1]/div/div/div[1]/div/form/div[2]/input")
    browser.execute_script("arguments[0].click();", browser.find_element(By.ID,"tnc"))
    submit = browser.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/form/input")

    name[0].send_keys("YOUR_UTMID")
    password[0].send_keys("YOUR_PASSWORD")
    submit[0].click()

    time.sleep(2)
    browser.close()
    
except:
    print("Error! Please make sure you are not logged in!")
