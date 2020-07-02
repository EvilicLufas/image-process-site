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


HOST_SITE_APIS = {
    'www.tiktok.com' : 'https://www.tiktok.com/oembed?url=',
    'www.youtube.com' : ''
}
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
"""Class to handle url requests from the user and access the given website's api to retrieve the video 
    Often gets blocked by tiktok from getting src tag.
"""
class RequestHandler():
    response = {}
    user_url = ''
    request_url = ''
    host_site = ''
    html_response = ''
    path = 'C:/Users/tznoo/Dev/image_process_site/static/temp_videos/downloaded_video.mp4'
    selenium_retries=0
    
    """ takes the url provided by the user and gets the proper api url and fetches a response and stores
        it in the response field 
    """
    def __init__(self,user_url=''):
        self.user_url = user_url
        self.hostSite(user_url)
        self.response = requests.get(self.request_url)
        self.setHTML()

    """ Method to print the response object
    """
    def printResponse(self):
        pprint(self.response.json())
    
    """ Method to determine the host site that the url is from and add the proper 
        api path to create the request URL
    """
    def hostSite(self, user_url=''):
        parsed_url = urlparse(user_url) 
        try:
            self.request_url = HOST_SITE_APIS[parsed_url[1]]+user_url
        except KeyError:
            print("API not available for the website " + str(user_url))
    def setHTML(self):
        self.html_response = self.response.json()['html']

    def getVideoSrc(self):
        response = requests.get(self.user_url, headers=headers)
        soup =  BeautifulSoup(response.text, features="lxml")
        video_soup = soup.find_all('video')
        print(response.status_code)
        print(video_soup)
        # print(soup.prettify())
        # page_html = html.fromstring(response.content)
        #response = .get(self.user_url)
        # print(page_html)

    def createVideoFile(self):
        # chromePath = 'C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/webdrivers/chromedriver.exe'
        firePath = 'C:/Webdrivers/geckodriver.exe'
        #setting the useragent
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Googlebot")
        #setting the driver to be in headless mode
        # options = Options()
        # options.add_argument('user-agent=Googlebot')
        options = webdriver.FirefoxOptions()
        options.headless=False
        #getting the webpage
        # driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=firePath)
        driver = webdriver.Firefox(profile, options=options, executable_path=firePath)

        driver.get(self.user_url)
        video = driver.find_element_by_tag_name('video') #finds video on tiktok page
        video_link = video.get_attribute("src")
        # driver.get(video.get_attribute("src")) #loads downloadable video page
        # video = driver.find_element_by_tag_name('video') #finds video on downloadable page
        resp = requests.get(video_link)
        with open(self.path, 'wb') as f:
            f.write(resp.content)
        driver.close()      