#!/usr/bin/python
from selenium import webdriver
import time
# disable push notification of chrome browser
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/usr/lib/chromium-browser/chromedriver")
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("email").send_keys("ReplaceWithYourUsername")
driver.find_element_by_id("pass").send_keys("ReplaceWithYourPassword")
driver.find_element_by_id("loginbutton").click()
driver.refresh()
# page scroll
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
i = 0
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # breasks loop if  reach end of webpage
    if new_height == last_height:
        break
    last_height = new_height
    # breaks loops
    i = i + 1
    if i == 2:
        break
##

# logout initiated
driver.find_element_by_id("logoutMenu").click()
driver.find_element_by_class_name("_64kz").click()
driver.get_screenshot_as_file("/home/kamal/Desktop/python/seleniumPython/scripts/facebook.png")
driver.quit()
