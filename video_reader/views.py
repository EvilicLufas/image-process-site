from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .forms import URLForm
from django.contrib import messages
# from request_handler.RequestHandler import RequestHandler
# from request_handler.Request import Request
from request_handler.RequestRaw import RequestRaw
from tf_pose_estimation.VideoAnalysis import VideoAnalysis
from django.views import View
from queue import Queue
import threading
import time


class FormView(View):
    form_class = URLForm
    initial = {'key':'value'}
    template_name = 'video_reader/home.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST['video_url'])
        if form.is_valid():
            request.session['video_url'] = form.video_url
            return HttpResponseRedirect('/url_rec/')
        else:
            print('did not enter valid url')
            return render(request, self.template_name, {'form':self.form_class()})


class ReceivedView(View):
    form_class = RequestRaw
    # form_class = RequestHandler
    template_processed = 'video_reader/analyzed.html'

    def get(self, request):
        context = self.analyze(request)
        return render(request, self.template_processed, context)

    def analyze(self, request):
        videoIDs = {}
        video_url = request.session.get('video_url')
        response = self.form_class(video_url, videoIDs)
        # response.createVideoFile() #for RequestHandler Class
        # response.get_selenium_res() #for Request Class
        id = response.download_video()
        path = 'C:/Users/tznoo/Dev/image_process_site/static/temp_videos/processed_video.mp4'
        AnalObj = VideoAnalysis(path)
        proc_id = AnalObj.poseAnalysis(id, response.PATH) #this returns the id for the processed video that's created
        return {"downloaded":response.PATH[45:],"processed":AnalObj.path[45:]}


class HowToView(View):
    template = 'video_reader/howto.html'

    def get(self, request):
        return render(request, self.template)