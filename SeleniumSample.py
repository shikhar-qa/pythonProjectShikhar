from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("https://www.saucedemo.com/")
browser.implicitly_wait(5)
browser.maximize_window()


class Loginpage():

    def verify_login_valid_user(self, uname, passwd):
        testcase = "Verify to login with valid user"
        result = ""
        self.uname = uname
        self.passwd = passwd

        try:
            searchtxt = browser.find_element("id", "user-name")
            searchtxt.send_keys("standard_user")
            passwdtxt = browser.find_element("id", "password")
            passwdtxt.send_keys("secret_sauce")
            loginbtn = browser.find_element("id", "login-button")
            loginbtn.click()

            get_source = browser.page_source
            if "Swag Labs" in get_source:
                print("Login successfully")
            else:
                print("Login failed")

            browse_btn = browser.find_element("id", "react-burger-menu-btn")
            browse_btn.click()

            logout_btn = browser.find_element("id", "logout_sidebar_link")
            logout_btn.click()
            result = "PASS"
        except Exception as e:
            result = "FAIL"
            print(e)

        return {"testcase": testcase, "result":result}


objloginpage = Loginpage()
status = objloginpage.verify_login_valid_user("standard_user", "secret_sauce")
print(status['testcase'] + ": " + status['result'])
