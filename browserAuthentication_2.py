#!/usr/bin/python
from selenium import webdriver
####### view dhcp client list of tp-link wireless router ###########
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://admin:admin@192.168.0.1/")
driver.maximize_window()
driver.set_page_load_timeout(30)
#switch to sidebar
driver.switch_to.frame("bottomLeftFrame")
driver.find_element_by_id("a13").click()
driver.find_element_by_id("a15").click()
#switch to main frame to get table data
#driver.switch_to.frame("mainFrame")
#r = driver.find_element_by_id("autoWidth")
#print(r)
#for row in driver.find_element_by_id("autoWidth"):
#    cell = row.find_elements_by_tag_name("td")[1]
#    #print(cell.text)
#driver.quit()
