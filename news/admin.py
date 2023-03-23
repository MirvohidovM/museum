from django.contrib import admin
from .models import News, NewsImages
from django.db import models
from django import forms
from tinymce.widgets import TinyMCE


class NewsImagesAdmin(admin.TabularInline):
    model = NewsImages
    extra = 1
    verbose_name = 'Янгилик Расми'
    verbose_name_plural = 'Янгилик Расмлари'
    # formfield_overrides = {
    #     models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    # }


class NewsForm(forms.ModelForm):
    content_uz = forms.CharField(label='Матн [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label='Матн [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    content_ru = forms.CharField(label='Матн [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label='Матн [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    class Meta:
        model = News
        exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']


class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    ordering = ('-pub_date',)
    form = NewsForm

    list_filter = ['is_active', ]
    list_display = ['title_uz', 'pub_date', 'is_active']
    search_fields = ['title_ru', 'title_uz', 'title_uzb', 'title_en',
                     'content_uz', 'content_uzb', 'content_ru', 'content_en']
    exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']

    # filter_horizontal = ('',)
    inlines = [NewsImagesAdmin]
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "Ўчириш"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user

        obj.save()
        for filename, file in request.FILES.items():
            if filename == 'cover':
                continue
            pictures = request.FILES.getlist(filename)
            for picture in pictures[:-1]:
                NewsImages.objects.create(news=obj, image=picture)
        return super().save_model(request, obj, form, change)


admin.site.register(News, NewsAdmin)
