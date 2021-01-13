from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()

    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')

    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

