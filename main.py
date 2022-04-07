from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='YOURPATH' , options=option)

browser.get("http://1.1.1.2/")

id = browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[1]/input")
password = browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[2]/input")
browser.execute_script("arguments[0].click();", browser.find_element(By.ID,"tnc"))
submit = browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/input")

id[0].send_keys("YOURUTMID")
password[0].send_keys("YOURPASSWORD")
submit[0].click()

time.sleep(2)
browser.close()
