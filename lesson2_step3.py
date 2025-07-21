from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Kiryl')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Kamenev')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('test@email.com')
    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_path = os.path.join(current_dir, 'dest.txt')
    element = browser.find_element(By.NAME, 'file')
    element.send_keys(file_path)
    button_press = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_press.click()
finally:
    time.sleep(20)
    browser.quit()
