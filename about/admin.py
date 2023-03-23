from django.contrib import admin
from .models import About, AboutImages
from solo.admin import SingletonModelAdmin
from django import forms
from tinymce.widgets import TinyMCE


class AboutImagesAdmin(admin.TabularInline):
    model = AboutImages
    can_delete = True
    extra = 1
    verbose_name = 'Расм'
    verbose_name_plural = 'Расмлар'


class AboutForm(forms.ModelForm):
    description_uz = forms.CharField(label='Музей тарихи [uz]',
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    description_uzb = forms.CharField(label='Музей тарихи [uzb]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)
    description_ru = forms.CharField(label='Музей тарихи [ru]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)
    description_en = forms.CharField(label='Музей тарихи [en]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = About
        fields = ['description_uz', 'description_uzb', 'description_ru', 'description_en']

    # exclude = (
    #     'description',
    #     'on_slider',
    # )


class AboutAdmin(SingletonModelAdmin):
    form = AboutForm
    fieldsets = (
        ("Умумий маълумот", {
            'fields': ('description_uz', 'description_uzb', 'description_ru', 'description_en',)
        }),
    )
    inlines = [AboutImagesAdmin]
    exclude = (
        'description',
        'on_slider',
    )
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "Ўчириш"


admin.site.register(About, AboutAdmin)
