from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import sys



from selenium.webdriver.common.keys import Keys
import os

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://kiitportal.kiituniversity.net/irj/portal/")
driver.implicitly_wait(15)

ids = driver.find_elements(By.ID, "logonuidfield")

id = driver.find_element(By.XPATH, "//input[@id='logonuidfield']").send_keys("") #enter roll no. inside quotes
password = driver.find_element(By.ID, 'logonpassfield').send_keys("") #enter password inside quotes
login = driver.find_element(By.XPATH, "//input[@class='urBtnStdNew']").click()
driver.find_element(By.LINK_TEXT,
                    'Student Self Service for Computer Science & Systems Engineering (CSSE - 2020 Batch)').click()


driver.switch_to.frame("ivuFrm_page0ivu3")
driver.find_element(By.LINK_TEXT, 'Student Self Service').click()


attendance = driver.find_element(By.LINK_TEXT, 'Student Attendance Details')

try:
    attendance.click()
except StaleElementReferenceException:
    attendance = driver.find_element(By.LINK_TEXT, 'Student Attendance Details')
    attendance.click()

driver.switch_to.frame('isolatedWorkArea')
ele = driver.find_element(By.ID, 'WD52').click()
driver.find_element(By.ID, 'WD64').click()

driver.find_element(By.ID, 'WD6E').click()
driver.find_element(By.ID, 'WD71').click()
driver.find_element(By.ID, 'WD7B').click()

driver.maximize_window()

driver.execute_script("document.body.style.zoom = '125%'")


driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)

driver.save_screenshot("s1.png")

time.sleep(60)
driver.quit()
