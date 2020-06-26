from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
import requests

class Request:
    selenium_retries = 0
    path = 'C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/static/temp_videos/downloaded_video.mp4'

    def __init__(self, url):
        self.url = url

    def get_selenium_res(self):
        try:
            software_names = [SoftwareName.FIREFOX.value]
            operating_systems = [OperatingSystem.WINDOWS.value,
                                OperatingSystem.LINUX.value]
            user_agent_rotator = UserAgent(software_names=software_names,
                                           operating_systems=operating_systems,
                                           limit=100)
            user_agent = user_agent_rotator.get_random_user_agent()
            firefox_options = Options()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--window-size=1420,108-")
            firefox_options.add_argument("--disable-gpu")
            firefox_options.add_argument(f'user-agent={user_agent}')
            firefox_options.binary ='C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/webdrivers/geckodriver.exe'
            firefox_options.profile = webdriver.FirefoxProfile()


            PROXY = "https://159.8.114.34"
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.autodetect = False
            capabilities = webdriver.DesiredCapabilities.FIREFOX
            prox.http_proxy = PROXY
            prox.ssl_proxy = PROXY
            prox.add_to_capabilities(capabilities)

            #browser = webdriver.Firefox(options=firefox_options, desired_capabilities=capabilities) #initializing browser with the proxy
            #proxies are easily blocked after multiple uses-so not using it
            browser = webdriver.Firefox(options = firefox_options) #initializing browser without proxy

            browser.get(self.url)
            time_to_wait = 90
            tag_name = 'video'
            try:
                WebDriverWait(browser, time_to_wait).until(
                    EC.presence_of_element_located((By.TAG_NAME, tag_name)))
            finally:
                browser.maximize_window()
                video = browser.find_element_by_tag_name(tag_name)
                video_link = video.get_attribute('src')
                resp = requests.get(video_link)
                with open(self.path,'wb') as f:
                    f.write(resp.content)
                browser.close
                print("video written")
        except (TimeoutException):
            print("You were likely blocked")
            self.selenium_retries+=1
            return self.get_selenium_res()
        except (WebDriverException):
            print("Something went wrong with the web driver")


      