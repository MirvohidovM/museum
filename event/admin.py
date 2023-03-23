from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE

from .models import *


class EventImagesAdmin(admin.TabularInline):
    model = EventImages
    extra = 1
    verbose_title = 'Тадбир Расми'
    verbose_title_plural = "Тадбир Расмлари"
    # formfield_overrides = {
    #     models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    # }


class EventForm(forms.ModelForm):
    content_uz = forms.CharField(label="Матн [uz]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label="Матн [uzb]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_ru = forms.CharField(label="Матн [ru]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label="Матн [en]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    class Meta:
        model = Event
        exclude = ['created_by', 'updated_by', 'slug', 'views', 'title', 'content']


class EventAdmin(admin.ModelAdmin):
    ordering = ['-start_time']
    exclude = ['created_by', 'updated_by', 'slug', 'title',
               'content', 'main_topic', 'responsible_org', 'address', 'views']
    list_display = ["title_uz", "title_ru",
                    'start_time', 'end_time', 'is_active']
    list_filter = ['is_active',]
    search_fields = ["title_uz", "title_ru", "title_uzb", "title_en"]
    inlines = [EventImagesAdmin]
    form = EventForm


class EventTypeAdmin(admin.ModelAdmin):
    exclude = ['title', 'slug', 'created_by', 'updated_by']


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
# admin.site.register(EventImages)
