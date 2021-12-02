import time
import requests
import pyfiglet
from mainfile import name

banner = pyfiglet.figlet_format(name)
print(banner)

msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Please Insert WebHook URL: ")

def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
mal_top = 1
while mal_top == 1:
    spam(msg, webhook)