from selenium.webdriver.common.by import By
import time

from test.config.url_constants import HOME_PAGE_URL, LOGIN_URL, SIGN_UP_URL



def goToSignUpPage(context):
    assert(context.driver)
    driver = context.driver
    assert(driver.current_url == LOGIN_URL or driver.current_url == HOME_PAGE_URL)
    driver.find_element(By.ID, 'signup').click()
    time.sleep(1)
    assert(driver.current_url  == SIGN_UP_URL)
    

    