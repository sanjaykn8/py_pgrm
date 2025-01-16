from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/nisan/Downloads/Programs/edgedriver_win64/msedgedriver.exe", verbose=False)
driver = webdriver.Edge(service=service)

try:
    driver.get("https://www.instagram.com")
    time.sleep(5)  

    user_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    user_field.send_keys('___kn__._')

    pass_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    pass_field.send_keys('$@njayKN008')

    log_but = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
    log_but.click()

    input()
    
finally:
    driver.quit()