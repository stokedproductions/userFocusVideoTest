from django.shortcuts import render

from django.http import HttpResponse

from videoClipLibrary.models import SourceVideo, MarkedTimeStamp


def index(request):
    videos = SourceVideo.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'HomeTemplate.html', context)