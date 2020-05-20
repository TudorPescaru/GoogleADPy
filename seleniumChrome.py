#! /usr/bin/env python

from selenium import webdriver


def send_text_to_input(input_name, text):    
    name = driver.find_element_by_name(input_name)
    name.send_keys(text)


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver.maximize.window()
driver.get("https://www.cel.ro/index.php?main_page=login")
send_text_to_input('firstname', 'Test')
send_text_to_input('lastname', 'Test')
send_text_to_input('email_address', 'test@gmail.com')
send_text_to_input('telephone', '0123456789')
send_text_to_input('telephone', '0123456789')

