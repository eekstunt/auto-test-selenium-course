from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()

    browser.get(link)

    x1 = int(browser.find_element_by_id('num1').text)
    x2 = int(browser.find_element_by_id('num2').text)

    y = str(x1 + x2)

    select = Select(browser.find_element_by_id('dropdown'))
    option = select.select_by_visible_text(y)

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

