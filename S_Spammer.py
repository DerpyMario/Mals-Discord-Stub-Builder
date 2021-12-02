import pyautogui, time
import pyfiglet
from mainfile import name

banner = pyfiglet.figlet_format(name)
print(banner)

msg = input("Enter your message: ")
times = input("How many time do you want to do this?( 0 for inf ): ")

print("t minus")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

if times.startswith('0'):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")

for repeat in range(0, int('times')):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")