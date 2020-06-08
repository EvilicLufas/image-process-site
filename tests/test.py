from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests
import cv2 as cv

#webdriver test code
        # page = 'https://www.tiktok.com/@letdogfun/video/6831938226542873861?lang=en'
        # chromePath = r'C:/Users/tznoo/Envs/ImageProcess/image_process_site/webdrivers/chromedriver.exe'
        # firePath = r'C:/Users/tznoo/Envs/ImageProcess/image_process_site/webdrivers/geckodriver.exe'
        # #driver = webdriver.Chrome(executable_path=chromePath)
        # #setting the useragent
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("general.useragent.override", "Googlebot")
        # #setting the driver to be in headless mode
        # options = webdriver.FirefoxOptions()
        # options.headless=True
        # #getting the webpage
        # driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=firePath)
        # driver.get(page)
        # video = driver.find_element_by_tag_name('video') #finds video on tiktok page
        # video_link = video.get_attribute("src")
        # # driver.get(video.get_attribute("src")) #loads downloadable video page
        # # video = driver.find_element_by_tag_name('video') #finds video on downloadable page
        # resp = requests.get(video_link)
        # with open("downloaded_video.mp4", 'wb') as f:
        #     f.write(resp.content)
        # driver.close()

#video size test code
# widePath = 'C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/'
# tallPath = 'C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/temp_videos/downloaded_video.mp4'
tallPath = './temp_videos/downloaded_video.mp4'
cap = cv.VideoCapture(tallPath)
print("height = " + str(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print("width = " + str(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
wide = True
w = int(width/2)
h = int(height/2)
newWidth = round(height*432/358)

# if (height > width):
#     newWidth = round(height*358/432)
#     wide = False
#     h = 432
#     w = 368

if cap.isOpened() is False:
    print("Error opening video stream or file")
while cap.isOpened():
    ret_val, image = cap.read()
    if ret_val:
        #image = image[0:height, (0+((width-newWidth)//2)):(width-((width-newWidth)//2))]
        image = cv.resize(image, (w,h),fx=0,fy=0,interpolation=cv.INTER_AREA)
        cv.imshow('resized', image)
        if cv.waitKey(1) == 27:
            break

cap.release()
cv.destroyAllWindows()

    
