from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_find = browser.find_element(By.ID, "num1")
    num2_find = browser.find_element(By.ID, "num2")
    num1 = int(num1_find.text)
    num2 = int(num2_find.text)
    sum1 = num1 + num2
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum1))
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(20)
    browser.quit()
