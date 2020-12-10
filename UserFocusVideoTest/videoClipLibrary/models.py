from django.db import models

# Create your models here.
class SourceVideo(models.Model):
    filename = models.FileField(upload_to='uploads/')
    pub_date = models.DateTimeField('date published')


class MarkedTimeStamp(models.Model):
    video = models.ForeignKey(SourceVideo, on_delete=models.CASCADE)
    marker_text = models.CharField(max_length=500)
    time_stamp_start = models.IntegerField() # this is stored in seconds
    time_stamp_end = models.IntegerField() # this is stored in seconds
    video_path = models.CharField(max_length=200, blank=True, null=True)
    