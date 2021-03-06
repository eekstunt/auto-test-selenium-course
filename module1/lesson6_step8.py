from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()

    browser.get(link)

    x = browser.find_element_by_id('input_value').text

    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

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

