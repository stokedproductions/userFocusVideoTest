""" Helper File to Split Videos """
from django.conf import settings as djangoSettings

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def video_splitter(source_video, split_times):
    for time in split_times:
        starttime = int(time.time_stamp_start)
        endtime = int(time.time_stamp_end)
        vfile = "uploads" + "/video" + str(source_video.id) + "-" + str(time.id) + ".mp4"
        ffmpeg_extract_subclip(str(source_video.filename), starttime, endtime, targetname=vfile)
        time.video_path = vfile
        time.save()