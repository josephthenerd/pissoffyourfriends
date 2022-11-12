import pyautogui as pg
import time
    
    
        
time.sleep(2)

with open("chat.txt", "r") as ext_file:
    for line in ext_file:
        splited = line.replace('\t', '    ')
        pg.write(splited)
        print(splited)
        time.sleep(0)
