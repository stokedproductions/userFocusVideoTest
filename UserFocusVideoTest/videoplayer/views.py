from django.shortcuts import render

from django.http import HttpResponse

from videoClipLibrary.models import SourceVideo, MarkedTimeStamp


def index(request, id):
    video = SourceVideo.objects.get(id=id)
    time_stamps = MarkedTimeStamp.objects.filter(video=id)
    context = {
        'video': video,
        'timestamps': time_stamps
    }
    return render(request, 'VideoTemplate.html', context)
