from selenium import webdriver #Intial setup
#from selenium.webdriver.chrome.service import Service  ##If I had chrome LOL
from selenium.webdriver.common.by import By #Used to find elements in HTML
from selenium.webdriver.common.keys import Keys #Used for Key Actions
from selenium.webdriver.firefox.service import Service #Intial setup
from selenium.webdriver.support.ui import WebDriverWait #Wait for some X seconds
from selenium.webdriver.support import expected_conditions as EC #What to wait for
import time

service = Service(executable_path="./geckodriver")
driver = webdriver.Firefox(service=service)

# get to a website 
driver.get("https://www.duckduckgo.com")

# Wait using WebDriverWait for element to exist within time with EC 
# for 5 seconds if doesnt exist within time frame crash

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'searchbox_input__rnFzM'))
)

# Find Search Box using By.CLASS_NAME 
input_box = driver.find_element(By.CLASS_NAME, 'searchbox_input__rnFzM')

#Clear any text and send text and press Enter Key
input_box.clear()
input_box.send_keys("Kabeer Shariff Github" + Keys.ENTER)

#Wait again
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "kabeershariff (Omar Shariff)"))
)

#Clicking on a link with partial text match
link = driver.find_element(By.PARTIAL_LINK_TEXT, "kabeershariff (Omar Shariff)")
link.click()

#pause 
time.sleep(3)

#quit
driver.quit()
