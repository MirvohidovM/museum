from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django import forms
from  tinymce.widgets import TinyMCE

from .models import Contact, LandmarkPhotos


class LandmarkPhotosAdmin(admin.TabularInline):
    model = LandmarkPhotos
    can_delete = True
    extra = 1
    exclude = ('name',)


class ContactForm(forms.ModelForm):
    address_uz = forms.CharField(label='Манзил [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    address_uzb = forms.CharField(label='Манзил [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    address_ru = forms.CharField(label='Манзил [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    address_en = forms.CharField(label='Манзил [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    transport_uz = forms.CharField(label='Транспорт [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    transport_uzb = forms.CharField(label='Транспорт [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    transport_ru = forms.CharField(label='Транспорт [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    transport_en = forms.CharField(label='Транспорт [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    phone = forms.CharField(label='Телефон [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    email = forms.CharField(label='Email почта [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),)

    class Meta:
        model = Contact
        exclude = ['address', 'transport']


class ContactAdmin(SingletonModelAdmin):
    exclude = ['address', 'transport']
    inlines = [LandmarkPhotosAdmin]
    form = ContactForm

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "Ўчириш"


admin.site.register(Contact, ContactAdmin)
