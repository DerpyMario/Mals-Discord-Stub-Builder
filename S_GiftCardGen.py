import time
import random
import pyfiglet
from mainfile import name


# functions
def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result

banner = pyfiglet.figlet_format(name)
print(banner)

# interface
print("Multiple Gift Card Generator")
print("")
print("What Giftcard you need to generate?")

tt = input(
    "\nAmazon\nRoblox\nWebkinz\nFortnite\nIMVU\nEbay\nNetflix\niTunes\nPaypal\nVisa\nPokemonTGC\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n\n>")

t = tt.lower()
print("")
print("How many of them?")
nn = input(">")
print("")
print("join here https://discord.gg/qqExcWPkJ4")
n = int(nn)

if t == "minecraft":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(4) + "-" + g(4))

if t == "paypal":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(4) + "-" + g(4))

if t == "playstation":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(4) + "-" + g(4))

if t == "amazon":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(6) + "-" + g(4))

if t == "netflix":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(6) + "-" + g(4))

if t == "steam":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(6) + "-" + g(5))

if t == "fortnite":
    for x in range(n):
        print("")
        print(g(5) + "-" + g(4) + "-" + g(4))

if t == "robolox":
    for x in range(n):
        print("")
        print(g(3) + "-" + g(3) + "-" + g(4))

if t == "itunes":
    for x in range(n):
        print("")
        print(g(16))

if t == "ebay":
    for x in range(n):
        print("")
        print(g(10))

if t == "imvu":
    for x in range(n):
        print("")
        print(g(10))

if t == "webkinz":
    for x in range(n):
        print("")
        print(g(8))

if t == "pokemontgc":
    for x in range(n):
        print("")
        print(g(3) + "-" + g(4) + "-" + g(3) + "-" + g(3))

if t == "playstore":
    for x in range(n):
        print("")
        print(g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4))

if t == "xbox":
    for x in range(n):
        print("")
        print(g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5))

print("")
print("-----Generation completed-----")
print("----https://discord.gg/qqExcWPkJ4----")
time.sleep(360)