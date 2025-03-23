from test.config.url_constants import LOGIN_URL, CONTACT_LIST_LANDING_PAGE_URL, SIGN_UP_URL, HOME_PAGE_URL
from selenium.webdriver.common.by import By

import time

from test.config.constants import TEST_USER_PASSWORD, TEST_USER_USERNAME

def loadLoginPage(context):
    assert(context.driver)
    driver = context.driver
    driver.get(HOME_PAGE_URL)

def goToSignUpPage(context):
    assert(context.driver)
    driver = context.driver
    assert(driver.current_url == LOGIN_URL or driver.current_url == HOME_PAGE_URL)
    driver.find_element(By.ID, 'signup').click()
    time.sleep(1)
    assert(driver.current_url  == SIGN_UP_URL)

def attemptLoginAsTestUser(context):
    context.username = TEST_USER_USERNAME
    context.password = TEST_USER_PASSWORD
    attemptloginAs(context)

def attemptLoginAsBadUser(context):
    context.username = TEST_USER_USERNAME
    context.password = "xxx" + TEST_USER_PASSWORD + "xxx"
    attemptloginAs(context)

def attemptloginAs(context):
    assert(context.driver)
    driver = context.driver
    assert(driver.current_url == LOGIN_URL or driver.current_url == HOME_PAGE_URL)
    userName = context.username
    password = context.password
    assert(userName)
    assert(password)
    driver.find_element(By.ID, 'email').send_keys(userName)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)

def verifyLoginSuccess(context):
    driver = context.driver
    assert(driver.current_url  == CONTACT_LIST_LANDING_PAGE_URL)

def verifyLoginFailure(context):
    driver = context.driver
    assert(driver.current_url == LOGIN_URL or driver.current_url == HOME_PAGE_URL)
    errorSpan = driver.find_element(By.CSS_SELECTOR, 'span#error')
    assert(errorSpan.text == 'Incorrect username or password')

def loginAs(context):
    attemptloginAs(context)
    verifyLoginSuccess(context)