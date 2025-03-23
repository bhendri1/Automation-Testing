from selenium import webdriver

def createDriver(context):
    context.driver = webdriver.Chrome()

def closeDriver(context):
    if context.driver:
        context.driver.quit()
        context.driver = None