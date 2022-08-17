from pyparsing import javaStyleComment
from selenium import webdriver
import time
import getpass

from selenium.webdriver.common.by import By

login = input('Qual é o login? ')
senha = getpass.getpass(prompt='Qual é a senha? ')

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.instagram.com')
time.sleep(2)
#########################   login     ##########################
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)

###################        Primeiro "not Now"    #############
driver.find_element(By.XPATH ,'//*[contains(concat( " ", @class, " " ), concat( " ", "y3zKF", " " ))]').click()
time.sleep(3)

###################### Segundo "not now"          #######
driver.find_element(By.XPATH ,'//*[contains(concat( " ", @class, " " ), concat( " ", "_a9_1", " " ))]').click()
time.sleep(4)

###################### Clica no Primeiro Story ############
driver.find_element(By.XPATH ,'//*[contains(concat( " ", @class, " " ), concat( " ", "_aama", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_aa8j", " " ))]').click()
time.sleep(4)

###################### Curti o story ####################
driver.find_element(By.XPATH , '//div[@class="_abx4"]//button[@type="button"]').click()
time.sleep(4)

driver.close()