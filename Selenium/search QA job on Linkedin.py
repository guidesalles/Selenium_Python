from selenium import webdriver
import time

from selenium.webdriver.common.by import By

login = input("Qual seu Login? ")
senha = input("Qual a sua senha? ")

driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/')
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'input__input').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="ember20"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'div input').send_keys("quality assurance test analyst")
driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]').click()

time.sleep(0.5)
