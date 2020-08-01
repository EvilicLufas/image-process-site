import requests
from django.core.cache import cache
import random

#Class that takes the raw video src link from video attribute and downloads the video
class RequestRaw:
    PATH = 'C:/Users/tznoo/Dev/image_process_site/static/temp_videos/downloaded_video.mp4'

    def __init__(self,url,idset,driver_type = 'firefox'):
        self.url = url
        self.driver_type = driver_type
        self.idset = idset

    def download_video(self):
        resp = requests.get(self.url)
        id = RequestRaw.uniqueID(self.idset)
        self.PATH = self.PATH.split(".")[0]+id+".mp4"
        with open(self.PATH,'wb') as f:
            f.write(resp.content)
            # cache.add(id, f) cannot cache videos
        print("video saved to file %s" % self.PATH)
        return id
        

    @staticmethod
    def uniqueID(idset):
        id = ""
        for x in range(16):
            id = id + str(random.randint(0,9))
        if id in idset:
            RequestRaw.uniqueID()
        else:
            return id