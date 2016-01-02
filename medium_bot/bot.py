import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import FACEBOOK_USERNAME, FACEBOOK_PASSWORD

from selenium.webdriver.support.wait import WebDriverWait


def wait_until_item(driver, item_id):
    WebDriverWait(driver, 10).until(
        lambda browser: browser.find_element_by_css_selector(item_id))

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)


def login(driver):
    try:
        if driver.logged_in:
            return driver
    except:
        pass
    driver.get("http://www.medium.com")
    driver.find_element_by_xpath('//a[@data-action="sign-in-prompt"]').click()
    driver.find_element_by_xpath('//button[@data-action="facebook-auth"]').click()
    wait_until_item(driver, '#email')
    driver.find_element_by_id("email").send_keys(FACEBOOK_USERNAME)
    driver.find_element_by_id("pass").send_keys(FACEBOOK_PASSWORD)
    driver.find_element_by_id("pass").send_keys(Keys.RETURN)

    wait_until_item(driver, '.postArticle-footer')
    driver.logged_in = True
    return driver


def follow_user(user_id, driver):
    driver = login(driver)
    driver.get("http://medium.com/@{0}/".format(user_id))
    driver.find_element_by_xpath('//button[@data-action="toggle-subscribe-user"]').click()
    return True

if sys.argv[1] == "follow":
    follow_user(user_id=sys.argv[2], driver=driver)
