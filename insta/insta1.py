from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/nisan/Downloads/Programs/edgedriver_win64/msedgedriver.exe", verbose=False) #Replace my path with yours
driver = webdriver.Edge(service=service)

try:

    #I used edge. So for safety copy XPath again form your browser
    
    driver.get("https://www.instagram.com")
    time.sleep(5)  

    user_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    user_field.send_keys('username')  #Put your username here

    pass_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    pass_field.send_keys('password')  #Put your password here

    log_but = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
    log_but.click()

    input()
    
finally:
    driver.quit()
