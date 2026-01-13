
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : open https://kaneai-playground.lambdatest.io/
    driver.get("https://kaneai-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Click on the Enable Notification label in the notification toggle section
    element_locators = ['.card > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1)', '.card > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1)', "//h3[text()='Enable Notification']", "//h3[contains(text(),'Enable Notification')]", "//div[contains(@class,'card')]/div[1]/div[1]/h3[1]", "//div[contains(@class,'card')]/div[1]/div[1]/h3[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Open objective URL https://ecommerce-playground.lambdatest.io
    driver.get("https://ecommerce-playground.lambdatest.io")
    driver.implicitly_wait(6)

    # Step - 4 : Click on the search input field with placeholder 'Search For Products' in the top center
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Type in search input field in the top center 'iphone'
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'iphone':
            element.send_keys(char)
    else:
        element.send_keys('iphone')
    driver.implicitly_wait(6)

    # Step - 6 : Press enter in search input field with placeholder 'Search For Products'
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    element.send_keys('ENTER')
    driver.implicitly_wait(6)

    # Step - 7 : Scroll in document
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 8 : Scroll in document
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 9 : Click on the iPhone product image with action icons in the product grid
    element_locators = ["//a[@id='mz-product-grid-image-79-212469']/div[1]/div[1]/img[1]", "//a[@id='mz-product-grid-image-79-212469']/div[1]/div[1]/img[1]", '#mz-product-grid-image-79-212469 > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)', '#mz-product-grid-image-79-212469 > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on the 'ADD TO CART' button next to quantity selector
    element_locators = ["//div[@id='entry_216842']/button[1]", "//div[@id='entry_216842']/button[1]", '#entry_216842 > button', '#entry_216842 > button:nth-child(1)', '#entry_216842 > button:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Click on the Checkout button in the cart popup
    element_locators = ["//a[contains(text(),'Checkout')]", '.toast > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)', '.toast > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)', "//div[contains(@class,'toast') and contains(@class,'fade') and contains(@class,'show')]/div[2]/div[2]/div[2]/a[1]", "//div[contains(@class,'toast') and contains(@class,'fade') and contains(@class,'show')]/div[2]/div[2]/div[2]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
