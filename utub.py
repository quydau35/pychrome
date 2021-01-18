import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = '/home/quyngan/Downloads/chromedriver'

user_names_file = './usernames.txt'
video_url = 'https://www.youtube.com/watch?v=IlHrdsPXOUM'
video_interval_length = 5*60+41
usernames = open(user_names_file, "r").read().split("\n")
print( video_interval_length )
n = 0
while True:
    print("username: " + str(usernames[n]))
    options = webdriver.ChromeOptions()
    options.add_argument("--autoplay-policy=no-user-gesture-required")
    options.add_argument("--user-data-dir=users/" + str( usernames[n] ))
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.get(video_url)
    for i in range(5):
        print("loop: " + str(i) + " times")
        time.sleep(3)
        time.sleep(video_interval_length)
        driver.refresh()
    driver.close()
# driver.reload()
