from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
    summ = int(x1)+int(x2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(summ))

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
