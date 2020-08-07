from threading import Thread
import os
import socket
import time

class VideoManager(Thread):

    def __init__(self):
        super(VideoManager, self).__init__()
        self.videos = {}
        self.path = "C:/Users/tznoo/Dev/image_process_site/static/temp_videos"
    
    # method to add videos to the video manager dictionary, adds the video along with a timestamp
    # the video title is the key and the value is the timestamp
    def addVideo(self, video):
        ts = time.time()
        self.videos[video] = ts
   
    # method to delete videos in the temp directory after a set period of time
    # takes no parameters and returns nothing
    def deleteVideos(self):
        if len(self.videos)!=0:
            ts = time.time()
            length = len(self.videos)
            keys = []
            for video in self.videos:
                time_dif = (ts - self.videos[video])/60 #difference in minutes
                if time_dif>=1:
                    os.remove(os.path.join(self.path, video))
                    keys.append(video)
            for key in keys:
                self.videos.pop(key)
                print("video deleted")
        else:
            print("no videos to delete")

    # run method will continually delete videos while running
    def run(self):
        while(True):
            print("scanning video files to be deleted")
            time.sleep(3*60)
            self.deleteVideos()