from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("window.scrollBy(0, 100);", button)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    checkbox_find = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_find.click()
    radiobutton_find = browser.find_element(By.ID, 'robotsRule')
    radiobutton_find.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
