import requests

#Class that takes the raw video src link from video attribute and downloads the video
class RequestRaw:
    PATH = 'C:/Users/tznoo/OneDrive/Documents/Code Projects/image_process_site/static/temp_videos/downloaded_video.mp4'

    def __init__(self,url,driver_type = 'firefox'):
        self.url = url
        self.driver_type = driver_type

    def download_video(self):
        resp = requests.get(self.url)
        with open(self.PATH,'wb') as f:
            f.write(resp.content)
        print("video written")