from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import URLForm
from django.contrib import messages
from image_process_site.request_handler.RequestHandler import RequestHandler
from tf_pose_estimation.VideoAnalysis import VideoAnalysis

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST['video_url'])
        if form.is_valid():
            request.session['video_url'] = form.video_url
            return HttpResponseRedirect('/url_received/')
        else:
            error_message = "Did not enter a valid url"
            #display a message indicating url is invalid
            return render(request, 'video_reader/home.html', {'form':URLForm(), 'error_message':error_message})
            #redirect back to home page
            # return HttpResponseRedirect('')
    #if a GET (or any other method) create a blank form
    else:
        form = URLForm()
    return render(request, 'video_reader/home.html', {'form':form})   

def url_received(request):
    video_url = request.session.get('video_url')
    response = RequestHandler(video_url)
    response.createVideoFile()
    path = 'C:\\Users\\tznoo\\Envs\\ImageProcess\\image_process_site\\temp_videos\\processed_video.mp4'
    VideoAnalysis(path).poseAnalysis(response.path)
    return render(request, 'video_reader/url_received.html', {'html':response.html_response})

#figure out how to make processing page
#apply pose estimation and change video speed (look into changing video speed dynamcially)
#bring pose estimated video and original video into webpage to play.

