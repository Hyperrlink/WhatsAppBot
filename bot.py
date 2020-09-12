import seleniumbot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import re
from googlesearch import search
import time

# Path to ChromeDriver
PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'

# ID's of elements (Buttons, TextBoxed and more)
TEXTBOXNAME = '_3uMse'
MESSAGEBOXNAME = 'copyable-text'
TARGETNAMECHECK = '_210SC'
BUTTONNAME = '_1U1xa'
OUTMESSAGEBOXNAME = '_210SC'

BOTPREFIX = '*Jarvis:* '


def searchYouTube(whatToSearch):
    # Get a search term, search Youtube and retrns the URL of the first video
    query_string = urllib.parse.urlencode({"search_query": whatToSearch})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "http://www.youtube.com/watch?v=" + search_results[0]


def searchGoogle(whatToSearch):
    # Get a search term, search Google and retrns the URL of the first website
    results = search(whatToSearch, tld='com', lang='en',
                     num=1, start=0, stop=0, pause=2.0)
    for result in results:
        return result


def send(message):
    # Call seleniumbot.sendMessage() to send a message
    seleniumbot.sendMessage(
        msg=message, textBoxName=TEXTBOXNAME, buttonName=BUTTONNAME)


def executeCommand(message):
    # Get a command, cut it and process it
    command = message.split(' ')[0]
    command = command[1:].lower()
    parameter = ' '.join(message.split(' ')[1:])
    if command == 'here':
        output_message = BOTPREFIX + 'Why are you here?'
    elif command == 'bruh':
        output_message = BOTPREFIX + Keys.SHIFT + "\n" + \
            Keys.SHIFT + 'https://www.youtube.com/watch?v=2ZIpFytCSVc'
    elif command == 'yt' and parameter != '':
        url = searchYouTube(whatToSearch=parameter)
        output_message = BOTPREFIX + 'The YouTube url for ' + \
            parameter + ' is: ' + str(url)
    elif command == 'google' and parameter != '':
        url = searchGoogle(whatToSearch=parameter)
        output_message = BOTPREFIX + 'The Google url for ' + \
            parameter + ' is: ' + str(url)
    elif command == 'nword':
        output_message = BOTPREFIX + "You don't have the N-word pass."
    elif command == 'help':
        output_message = BOTPREFIX
        output_message += "_/here_ to get a respose. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += "_/nword_ to get the N-word pass." + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += " _/yt_ to search YouTube. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += " _/bruh_ because bruh. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += "_/google_ to search Google."
    else:
        output_message = BOTPREFIX + ' unknown command.'

    send(output_message)


def main():
    # Main method

    # Open chrome and get all the chats from WhatsApp
    seleniumbot.whatsappWebConnection(PATH, targetNameCheck=TARGETNAMECHECK)
    chats = seleniumbot.getChats(OUTMESSAGEBOXNAME)

    print(len(chats), "chats open")

    while True:
        # Loop on all the chats and gets the most recent message of each chat and calls executeCommand() if it's a command
        for chat in chats:
            chat.click()
            read_message = seleniumbot.getLastMessage(
                textDirection='')
            # Prefix '/' means that it's a command and not a regular message
            if read_message.startswith('/'):
                executeCommand(read_message)
            time.sleep(0.1)


if __name__ == '__main__':
    main()
