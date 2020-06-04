from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests

page = 'https://www.tiktok.com/@letdogfun/video/6831938226542873861?lang=en'
chromePath = r'C:/Users/tznoo/Envs/ImageProcess/image_process_site/webdrivers/chromedriver.exe'
firePath = r'C:/Users/tznoo/Envs/ImageProcess/image_process_site/webdrivers/geckodriver.exe'
#driver = webdriver.Chrome(executable_path=chromePath)
#setting the useragent
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Googlebot")
#setting the driver to be in headless mode
options = webdriver.FirefoxOptions()
options.headless=True
#getting the webpage
driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=firePath)
driver.get(page)
video = driver.find_element_by_tag_name('video') #finds video on tiktok page
video_link = video.get_attribute("src")
# driver.get(video.get_attribute("src")) #loads downloadable video page
# video = driver.find_element_by_tag_name('video') #finds video on downloadable page
resp = requests.get(video_link)
with open("downloaded_video.mp4", 'wb') as f:
    f.write(resp.content)
driver.close()
#this works!!