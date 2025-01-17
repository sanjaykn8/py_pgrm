from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-logging")  

service = Service(
    "C:/Users/nisan/Downloads/Programs/edgedriver_win64/msedgedriver.exe", # your path
    verbose=False,
    log_path="NUL"
)
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://www.instagram.com")
    
    user_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'))
    )
    user_field.send_keys('username')

    pass_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    pass_field.send_keys('password')

    log_but = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
    log_but.click()

    input() 

finally:
    driver.quit()
