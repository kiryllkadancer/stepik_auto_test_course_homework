from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    find_treasure = browser.find_element(By.ID, 'treasure')
    treasure_attr = find_treasure.get_attribute('valuex')
    x = treasure_attr
    y = calc(x)

    input_find = browser.find_element(By.ID, 'answer')
    input_find.send_keys(y)

    checkbox_find = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_find.click()

    radiobutton_find = browser.find_element(By.ID, 'robotsRule')
    radiobutton_find.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(20)
    browser.quit()
