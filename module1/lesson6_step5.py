from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()

    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')

    for element in elements:
        element.send_keys('Answer')

    submit_button = browser.find_element_by_class_name('btn')
    submit_button.click()

    time.sleep(5)

finally:
    browser.quit()

