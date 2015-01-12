#! python 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("hello")
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Common/chromedriver', chrome_options=chrome_options)

# driver = webdriver.Chrome('C:/Common/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
print(driver.title)
assert "Google" in driver.title
time.sleep(3)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1)  # Let the user actually see something!
search_box = driver.find_element_by_id('gbqfq')
search_box.clear()
search_box.send_keys('Python')
time.sleep(1)
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()


