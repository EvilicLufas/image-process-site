from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from time import sleep
from pprint import pprint
from urllib.parse import urlparse
import os
import random
import requests

#class that scrapes webpage for video tag and gets src attribute and downloads the video from it
#often gets blocked by tiktok
class Request:
    selenium_retries = 0
    path = 'C:/Users/tznoo/Dev/image_process_site/static/temp_videos/downloaded_video.mp4'

    def __init__(self, url, driver_type = 'firefox'):
        self.url = url
        self.driver_type = driver_type.lower()

    def setup_driver_options(self, user_agent):
        if self.driver_type == 'firefox':
            firefox_options = firefoxOptions()
            firefox_options.add_argument("--window-size=1420,1080")
            # firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
            firefox_options.add_argument(f'user-agent={user_agent}')
            # capabilities = self.setup_proxy(driver_type.lower())
            return firefox_options
        elif self.driver_type == 'chrome':#add more driver types (chrome, etc if necessary)
            chrome_options = chromeOptions()
            # chrome_options.add_argument("--headless")
            # chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--window-size=1420,1080")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument(f'user-agent={user_agent}')
            return chrome_options
        else:
            print("not supported driver type")

    def setup_proxy(self):
            PROXY = "159.8.114.34"
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.autodetect = False
            if self.driver_type =='firefox': #add more if you add more driver profiles above
                capabilities = webdriver.DesiredCapabilities.FIREFOX
            elif self.driver_type == 'chrome':
                capabilities = webdriver.DesiredCapabilities.CHROME
            prox.http_proxy = PROXY
            prox.ssl_proxy = PROXY
            prox.add_to_capabilities(capabilities)
            return capabilities

    def get_selenium_res(self):
        software_names = [SoftwareName.FIREFOX.value]
        operating_systems = [OperatingSystem.WINDOWS.value,
                            OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names,
                                        operating_systems=operating_systems,
                                        limit=100)
        user_agent = user_agent_rotator.get_random_user_agent()
        # user_agents = ['Googlebot','Applebot','Bingbot','DuckDuckBot','Naverbot','Twitterbot','Yandex']
        # user_agent = user_agents[random.randint(0, len(user_agents)-1)]
        print(user_agent)
        options = self.setup_driver_options(user_agent)
        #creating driver with a proxy:
            # browser = webdriver.Firefox(options=firefox_options, desired_capabilities=capabilities)
            #proxies are easily blocked after multiple uses-so not using it
        #initializing browser without proxy
        if self.driver_type=='firefox':
            browser = webdriver.Firefox(options = options) 
        elif self.driver_type == 'chrome':
            browser = webdriver.Chrome(chrome_options = options)
        browser.get(self.url)
        time_to_wait = 15
        tag_name = 'video'
        #locating element
        try:
            WebDriverWait(browser, time_to_wait).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name)))
            video = browser.find_element_by_tag_name(tag_name)
            video_link = video.get_attribute('src')
            resp = requests.get(video_link)
            with open(self.path,'wb') as f:
                f.write(resp.content)
            browser.close()
            print("video written")
        except TimeoutException:
            print("You were likely blocked")
            browser.close()
            self.selenium_retries+=1
            if self.driver_type == 'firefox':
                self.driver_type = 'chrome'
            else:
                self.driver_type = 'firefox'
            return self.get_selenium_res()
                
 

      