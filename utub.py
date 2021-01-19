import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import json

# chromedriver = '/home/liena/temp/selenium/chromedriver'

data = json.loads(requests.get(url="https://x1ai8s.deta.dev/all").text)

user_names_file = './usernames.txt'
video_url = 'https://www.youtube.com/watch?v=IlHrdsPXOUM'
video_interval_length = 5*60+41
usernames = open(user_names_file, "r").read().split("\n")
print( video_interval_length )
while True:
    n = random.randint( 0, len(usernames) - 1 )
    print("username: " + str(usernames[n]))
    for i in range(len(data[0])):
        options = webdriver.ChromeOptions()
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--headless")
        options.add_argument("--user-data-dir=users/" + str( usernames[n] ))
        driver = webdriver.Chrome( options=options)
        print(data[0][i]["url"])
        driver.get(data[0][i]["url"])
        for i in range(5):
            print("loop: " + str(i) + " times")
            time.sleep(3)
            time.sleep(video_interval_length)
            driver.refresh()
        driver.close()
        del driver
# driver.reload()
