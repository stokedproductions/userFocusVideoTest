from django.shortcuts import render
from django.http import HttpResponse

from videoClipLibrary.models import SourceVideo, MarkedTimeStamp

from .helps import video_splitter

def index(request, id):
    video_file = SourceVideo.objects.get(id=id)
    time_stamps = MarkedTimeStamp.objects.filter(video=id)
    print(video_file, time_stamps)

    video_splitter(video_file, time_stamps)
    context = {
        'orig_vid': video_file,
        'vid_snipts': time_stamps
    }
    return render(request, 'VideoSlippetsTemplate.html', context)
