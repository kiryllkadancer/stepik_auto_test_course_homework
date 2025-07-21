from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button_click = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'book'))
    )
    button_click.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_find = browser.find_element(By.ID, 'answer')
    input_find.send_keys(y)
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()
