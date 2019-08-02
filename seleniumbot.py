from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import threading
import time

driver = None


def whatsappWebConnection(chromeDriverPath, targetNameCheck):
    global driver

    chrome_options = Options()  # Saving the last session
    chrome_options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(chromeDriverPath, chrome_options=chrome_options)
    driver.get('https://web.whatsapp.com/')

    while True:
        time.sleep(1)
        try:
            # The class only exists after the QR login page
            appLoad = driver.find_element_by_class_name(targetNameCheck)
            if appLoad:
                return  # The login was successful
        except NoSuchElementException:
            pass


def sendMessage(msg, textBoxName, buttonName):
    msg_box = driver.find_element_by_class_name(textBoxName)
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name(buttonName)
    button.click()


def readAllMessages(textDirection, outMessageBox):
    global driver
    messages = None

    while(1):
        try:
            messages = driver.find_elements_by_xpath(
                '//span[@class="' + outMessageBox + '"]')
            return messages

        except (NoSuchElementException, StaleElementReferenceException) as e:
            return ''


def getLastMessage(textDirection):
    global driver
    messages = None

    while(1):
        try:
            messages = driver.find_elements_by_xpath(
                '//span[@dir="ltr"]')
            newMessage = messages[-1].text
            return str(newMessage)

        except (NoSuchElementException, StaleElementReferenceException) as e:
            return ''


def enterChat(targetName):
    targetName.click()


def getChats(targetName):
    global driver
    try:
        return driver.find_elements_by_class_name(targetName)
    except:
        pass
