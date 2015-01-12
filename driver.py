
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Common/chromedriver',
                          chrome_options=chrome_options)

driver.get('http://dev.com')
print(driver.title)
assert "INDY" in driver.title

travel = driver.find_element_by_xpath("//*[@id='yw1']/li[4]/a/i") 
travel.click()
time.sleep(1)

em = driver.find_element_by_xpath("//*[@id='content']/div[1]/div")
em.click()
time.sleep(1)

# em = driver.find_element_by_xpath("//*[@id='135627']/div[1]")  //*[@id="138631"]
em = driver.find_element_by_id('138631')
time.sleep(5)
em.click()
time.sleep(15)
driver.quit()

# em = driver.find_element_by_xpath("//*[@id='vert-tabs']/ul/li[3]/a")
# em.click()
# time.sleep(1)
#
# em = driver.find_element_by_id('newTrip')
# em.click()
# time.sleep(3)
#
# # input goes here for Travel Agents
# em = driver.find_element_by_id('agentDesc')
# em.send_keys('campbell')
# time.sleep(3)
#
# # input goes here for Notes
# em = driver.find_element_by_class_name('newRequestNotes')
# em.send_keys('This is some type of note or description about the trip.')
# time.sleep(3)
#
# em = driver.find_element_by_xpath("/html/body/div[6]/div[3]/i[2]"
#                                   "[@class='button close-button']")
# em.click()
# time.sleep(2)
#
# # TODO: get expected results
#
# driver.quit()

