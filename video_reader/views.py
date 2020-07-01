from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import URLForm
from django.contrib import messages
# from request_handler.RequestHandler import RequestHandler
# from request_handler.Request import Request
from request_handler.RequestRaw import RequestRaw
from tf_pose_estimation.VideoAnalysis import VideoAnalysis
from django.views import View

#figure out how to make processing page
#apply pose estimation and change video speed (look into changing video speed dynamcially)
#bring pose estimated video and original video into webpage to play.

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
    intial = {'key':'value'}
    template_name = 'video_reader/url_received.html'

    def get(self, request):
        video_url = request.session.get('video_url')
        response = self.form_class(video_url)
        # response.createVideoFile() #for RequestHandler Class
        # response.get_selenium_res() #for Request Class
        response.download_video()
        path = 'C:\\Users\\tznoo\\OneDrive\\Documents\\Code Projects\\image_process_site\\static\\temp_videos\\processed_video.mp4'
        AnalObj = VideoAnalysis(path)
        AnalObj.poseAnalysis(response.PATH)
        return render(request, self.template_name)
