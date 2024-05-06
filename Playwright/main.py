from playwright.sync_api import sync_playwright
import pandas as pd

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
context = browser.new_context(no_viewport=True)
page = context.new_page()
page.set_default_navigation_timeout(60000)

page.goto("https://rpachallenge.com/")

data = pd.read_excel('challenge.xlsx')

botao_iniciar = page.locator("xpath=/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

for index, row in data.iterrows():
    page.locator(f"xpath=//input[@ng-reflect-name='labelFirstName']").fill(row["First Name"])
    page.locator(f"xpath=//input[@ng-reflect-name='labelLastName']").fill(row["Last Name "])
    page.locator(f"xpath=//input[@ng-reflect-name='labelCompanyName']").fill(row["Company Name"])
    page.locator(f"xpath=//input[@ng-reflect-name='labelRole']").fill(row["Role in Company"])
    page.locator(f"xpath=//input[@ng-reflect-name='labelAddress']").fill(row["Address"])
    page.locator(f"xpath=//input[@ng-reflect-name='labelEmail']").fill(row["Email"])
    page.locator(f"xpath=//input[@ng-reflect-name='labelPhone']").fill(str(row["Phone Number"]))
    page.locator("xpath=html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

page.wait_for_timeout(5000)

page.screenshot(path='score_Playwright.png')
browser.close()