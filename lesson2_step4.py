from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_find = browser.find_element(By.ID, 'answer')
    input_find.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(20)
    browser.quit()
