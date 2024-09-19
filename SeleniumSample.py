from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("https://python.org")
browser.maximize_window()

searchtxt = browser.find_element("id", "id-search-field")
searchtxt.send_keys("sample")

searchBtn = browser.find_element("id", "submit")
searchBtn.click()
print(browser.title)


