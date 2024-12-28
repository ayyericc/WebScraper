from time import sleep
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as p: #Runs all the code inside the with statement and closes the browser after
    browser = p.chromium.launch(headless= False, slow_mo= 50)
    page = browser.new_page()
    page.goto("https://demo.opencart.com/admin/")
    page.fill(selector= "input#input-username", value= "demo")
    page.fill(selector= "input#input-password", value= "demo")
    page.click("button[type='submit']")
    page.is_visible("dive")
    html = page.inner_html("#content")
    print(html)



















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
#
# #keep chrome browser open
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options= chrome_options)
# driver.get("https://google.com")
#
#
# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.send_keys("Python dev jobs" + Keys.ENTER)
#













