import seleniumbot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import re
from googlesearch import search
import time

PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
TEXTBOXNAME = '_3uMse'
MESSAGEBOXNAME = 'copyable-text'
#TARGETNAMECHECK = '_2UaNq'
TARGETNAMECHECK = '_210SC'
BUTTONNAME = '_1U1xa'
#OUTMESSAGEBOXNAME = 'X7YrQ'
OUTMESSAGEBOXNAME = '_210SC'

BOTPREFIX = '*Jarvis:* '


def searchYouTube(whatToSearch):
    query_string = urllib.parse.urlencode({"search_query": whatToSearch})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "http://www.youtube.com/watch?v=" + search_results[0]


def searchGoogle(whatToSearch):
    results = search(whatToSearch, tld='com', lang='en',
                     num=1, start=0, stop=0, pause=2.0)
    for result in results:
        return result


def send(message):
    seleniumbot.sendMessage(
        msg=message, textBoxName=TEXTBOXNAME, buttonName=BUTTONNAME)


def executeCommand(message):
    command = message.split(' ')[0]
    command = command[1:].lower()
    parameter = ' '.join(message.split(' ')[1:])
    if command == 'gae':
        output_message = BOTPREFIX + 'Why are you gae?'
        send(output_message)
    elif command == 'bruh':
        output_message = BOTPREFIX + Keys.SHIFT + "\n" + \
            Keys.SHIFT + 'https://www.youtube.com/watch?v=2ZIpFytCSVc'
        send(output_message)
    elif command == 'yt' and parameter != '':
        url = searchYouTube(whatToSearch=parameter)
        output_message = BOTPREFIX + 'The YouTube url for ' + \
            parameter + ' is: ' + str(url)
        send(output_message)
    elif command == 'google' and parameter != '':
        url = searchGoogle(whatToSearch=parameter)
        output_message = BOTPREFIX + 'The Google url for ' + \
            parameter + ' is: ' + str(url)
        send(output_message)
    elif command == 'nigga':
        output_message = BOTPREFIX + "You don't have the N-word pass."
        send(output_message)
    elif command == 'help':
        output_message = BOTPREFIX
        output_message += "_/gae_ to get a gae respose. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += "_/nigga_ to get the N-word pass." + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += " _/yt_ to search YouTube. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += " _/bruh_ because bruh. " + Keys.SHIFT + "\n" + Keys.SHIFT
        output_message += "_/google_ to search Google."
        send(output_message)
    else:
        output_message = BOTPREFIX + ' unknown command.'
        send(output_message)


def main():
    seleniumbot.whatsappWebConnection(PATH, targetNameCheck=TARGETNAMECHECK)
    chats = seleniumbot.getChats(OUTMESSAGEBOXNAME)

    print(len(chats), "hello")

    while True:
        for chat in chats:
            chat.click()
            read_message = seleniumbot.getLastMessage(
                textDirection='')
            if read_message.startswith('/'):
                executeCommand(read_message)
            time.sleep(0.1)


if __name__ == '__main__':
    main()
