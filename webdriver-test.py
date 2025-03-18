from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USER_NAME = 'wyzant@gmail.com'
PASSWORD = 'Wyzant123'

HOME_PAGE_URL = 'https://thinking-tester-contact-list.herokuapp.com/'
LOGIN_URL = 'https://thinking-tester-contact-list.herokuapp.com/login'
SIGN_UP_URL = 'https://thinking-tester-contact-list.herokuapp.com/addUser'
CONTACT_LIST_LANDING_PAGE = 'https://thinking-tester-contact-list.herokuapp.com/contactList'

EMAIL_IN_USE_ERROR_MSG = 'Email address is already in use'


driver = webdriver.Chrome()
try:
    driver.get(HOME_PAGE_URL)

    driver.find_element(By.ID, 'signup').click()
    time.sleep(1)

    assert(driver.current_url ==  SIGN_UP_URL)

    assert(len(driver.find_elements(By.ID, 'error')) == 1)
    errorSpan = driver.find_element(By.CSS_SELECTOR, 'span#error')

    assert(len(errorSpan.text) == 0)

    driver.find_element(By.ID, 'firstName').send_keys('Name')
    driver.find_element(By.ID, 'lastName').send_keys('Johnson')
    driver.find_element(By.ID, 'email').send_keys(USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)

    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)

    if driver.current_url == SIGN_UP_URL:
        # user already exists
        assert(errorSpan.text == EMAIL_IN_USE_ERROR_MSG)
        driver.find_element(By.CSS_SELECTOR, 'button#cancel').click()
        assert(driver.current_url == LOGIN_URL)
        driver.find_element(By.ID, 'email').send_keys(USER_NAME)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        driver.find_element(By.ID, 'submit').click()

    time.sleep(1)
    print(f'driver.current_url        = "{driver.current_url}"')
    print(f'CONTACT_LIST_LANDING_PAGE = "{CONTACT_LIST_LANDING_PAGE}"')
    assert(driver.current_url  == CONTACT_LIST_LANDING_PAGE)
finally:
    driver.quit()