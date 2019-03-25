from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#import time

driver = webdriver.Chrome(r'''C:\Users\w\Desktop\chromedriver''')
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')
#in_xpath='//*[@id="pane-side"]/div/div/div/div[15]/div/div/div[2]/div[1]/div[1]/span/span'
#in_xpath='//*[@id="pane-side"]/div/div/div/div[13]/div/div/div[2]/div[1]/div[1]/span/span'
#above line is the xpath of jatin khare title, ctrl+shift +i
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#user = driver.find_element_by_xpath(in_xpath.format(name))
user.click()
class_name='_1Plpp'
msg_box = driver.find_element_by_class_name(class_name)

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()