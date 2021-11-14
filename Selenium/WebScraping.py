from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://curso-python-selenium.netlify.app/aula_03.html"

driver.get(url)

time.sleep(2)

a = driver.find_element(By.ID, 'ancora')


for click in range(10):
    p = driver.find_elements(By.TAG_NAME, "p")
    a.click()
    print(f'texto de p é {p[-1].text} e o valor do click é {click}')

time.sleep(1)
driver.quit()
