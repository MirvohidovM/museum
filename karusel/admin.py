from django.contrib import admin
from solo.admin import SingletonModelAdmin
# from django import forms
# from tinymce.widgets import TinyMCE

from .models import Karusel, KaruselImages


class KaruselImagesAdmin(admin.TabularInline):
    model = KaruselImages
    extra = 1
    verbose_name = 'Карусел расми'
    verbose_name_plural = 'Карусел расмлари'

    def has_delete_permission(self, request, obj=None):
        return True


# class KaruselForm(forms.ModelForm):
#     title_uz = forms.CharField(label='Mavzu [uz]',
#         widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
#     title_uzb = forms.CharField(label='Mavzu [uzb]', widget=TinyMCE(
#         attrs={'cols': 80, 'rows': 30}), required=False)
#     title_ru = forms.CharField(label='Mavzu [ru]', widget=TinyMCE(
#         attrs={'cols': 80, 'rows': 30}), required=False)
#     title_en = forms.CharField(label='Mavzu [en]', widget=TinyMCE(
#         attrs={'cols': 80, 'rows': 30}), required=False)
#
#     class Meta:
#         model = Karusel
#         fields = ['title_uz', 'title_uzb', 'title_ru', 'title_en']



class KaruselAdmin(SingletonModelAdmin):
    model = Karusel
    # form = KaruselForm
    exclude = ['title']
    list_display = ['title']
    inlines = [KaruselImagesAdmin]


admin.site.register(Karusel, KaruselAdmin)
