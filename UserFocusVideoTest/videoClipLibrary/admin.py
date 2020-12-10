from django.contrib import admin

from django.contrib import admin

from .models import SourceVideo, MarkedTimeStamp


class SourceVideoAdmin(admin.ModelAdmin):
    fields = ['filename', 'pub_date']

class MarkedTimeStampAdmin(admin.ModelAdmin):
    fields = ['video', 'marker_text', 'time_stamp_start', 'time_stamp_end', 'video_path']

admin.site.register(SourceVideo, SourceVideoAdmin)
admin.site.register(MarkedTimeStamp, MarkedTimeStampAdmin)
