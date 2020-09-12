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
    
    driver = webdriver.Chrome(chromeDriverPath, chrome_options=chrome_options) # Open Chrome as the bot
    driver.get('https://web.whatsapp.com/')  # Open WhatsApp Web in Chrome

    while 1:
        time.sleep(1)
        # Check if the user has logged in
        try:
            # The class only exists after the QR login page
            appLoad = driver.find_element_by_class_name(targetNameCheck)
            if appLoad:
                return  # The login was successful
        except NoSuchElementException:
            pass


def sendMessage(msg, textBoxName, buttonName):
    # Get a string that will be sent, a string of the ID of the textBox (it changes from time to time so it has to be hard codded)
    # and the ID of the send button
    msg_box = driver.find_element_by_class_name(
        textBoxName)  # Find the text box
    msg_box.send_keys(msg)  # Selenium types in the message that it has gotten
    button = driver.find_element_by_class_name(
        buttonName)  # Find the send button
    button.click()  # Click on the send button


# def readAllMessages(textDirection, outMessageBox):
#    global driver
#    messages = None
#
#    while(1):
#        try:
#            messages = driver.find_elements_by_xpath(
#                '//span[@class="' + outMessageBox + '"]')
#            return messages
#
#        except (NoSuchElementException, StaleElementReferenceException) as e:
#            return ''


def getLastMessage(textDirection):
    global driver
    messages = None

    while(1):
        try:
            messages = driver.find_elements_by_xpath(
                '//span[@dir="ltr"]')  # Find all the messages from a chat using their xpath
            # Get the last message that was sent
            newMessage = messages[-1].text
            return str(newMessage)  # Return the last message as a string

        except (NoSuchElementException, StaleElementReferenceException) as e:
            return ''  # Return an empty string if there was an error or if nothing was found


def enterChat(targetName):
    # Click on the chat it is given
    targetName.click()


def getChats(targetName):
    global driver
    try:
        # Return all the chat button elements
        return driver.find_elements_by_class_name(targetName)
    except:
        print("could not find chats")
