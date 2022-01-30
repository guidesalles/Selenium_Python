from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.instagram.com')
time.sleep(2)


driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('gorda_ex')
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('@Aa11091990aA@')
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)


driver.find_element(By.XPATH ,'/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(0.5)
driver.find_element(By.XPATH ,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('eusougabriela')
time.sleep(0.5)

driver.find_element(By.CLASS_NAME,"-qQT3").click()
