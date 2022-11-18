from bs4 import BeautifulSoup
import requests
import pyautogui
import time

def bot_spam(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    #print(parse)
    html = parse.find_all(tag)
    print(html)

    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press("enter")



bot_spam('http://127.0.0.1:5500/index.html', 'p')