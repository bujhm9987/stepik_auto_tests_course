import imp
from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("IPetrov@msx.sdf")

    input_file=browser.find_element_by_id('file')    
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir, 'testfile.txt')
    input_file.send_keys(file_path)

    btn1 = browser.find_element_by_css_selector('button.btn')
    btn1.click()


finally:
    time.sleep(10)
    browser.quit()