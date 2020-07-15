from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get('https://web.whatsapp.com/')
driver.implictly_wait(10)
user = driver.find_element_by_xpath('//span[@title = "Dhanush ECE"]')
user.click()
msgbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')
msgbox.send_keys('.')
send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
send.click()




