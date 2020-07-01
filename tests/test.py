from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriver

url = 'https://www.tiktok.com/@demibagby/video/6784536387992440070?lang=en'
driver = webdriver.Firefox()
driver.get(url)
time_to_wait = 90

WebDriverWait(driver, time_to_wait).until(EC.presence_of_element_located((By.TAG_NAME,'video')))
