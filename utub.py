import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process

import requests
import json

# chromedriver = '/home/liena/temp/selenium/chromedriver'

data = json.loads(requests.get(url="https://x1ai8s.deta.dev/all").text)

user_names_file = './usernames.txt'
video_url = 'https://www.youtube.com/watch?v=IlHrdsPXOUM'
video_interval_length = 5*60+41
usernames = open(user_names_file, "r").read().split("\n")
print( video_interval_length )

class Jobs:
    def __init__(self, url, interval, loop, active, username):
        self.url = url
        self.interval = interval
        self.loop = loop
        self.active = active
        self.username = username
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--autoplay-policy=no-user-gesture-required")
        self.options.add_argument("--headless")
        self.options.add_argument("--user-data-dir=users/" + str( self.username ))
        self.driver = webdriver.Chrome( options=self.options)

    def run_drivers(self, username):
        if (self.active):
            print(self.url)
            self.driver.get(self.url)
            for i in range(self.loop):
                print("loop: " + str(i) + " times")
                time.sleep(3)
                time.sleep(self.interval)
                self.driver.refresh()
                self.driver.close()
                del self.driver

for j in range(1000):
    n = random.randint( 0, len(usernames) - 1 )
    print("username: " + str(usernames[n]))
    job_list = []
    for i in range(len(data[0])):
        jb = Jobs(data[0][i]["url"], data[0][i]["video_interval_length"], data[0][i]["loop"], data[0][i]["active"], usernames[n])
        p = Process(target = jb.run_drivers(usernames[n]))
        job_list.append(p)
    for job_item in job_list:
        job_item.start()
        job_item.join()

# driver.reload()
