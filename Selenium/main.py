from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rpachallenge.com/")
driver.maximize_window()

data = pd.read_excel('challenge.xlsx')

botao_iniciar = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

for index, row in data.iterrows():
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelFirstName']").send_keys(row["First Name"])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelLastName']").send_keys(row["Last Name "])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelCompanyName']").send_keys(row["Company Name"])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelRole']").send_keys(row["Role in Company"])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelAddress']").send_keys(row["Address"])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelEmail']").send_keys(row["Email"])
    driver.find_element(By.XPATH, f"//input[@ng-reflect-name='labelPhone']").send_keys(row["Phone Number"])
    driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

time.sleep(5)

driver.save_screenshot('./score_selenium.png')
driver.close()