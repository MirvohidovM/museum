from django.contrib import admin, messages
from django import forms
from django.db import models
from django.http import HttpResponseRedirect

from gallery.models import PhotoGalleryImages, PhotoGallery


class PhotoGalleryImagesAdmin(admin.TabularInline):
    model = PhotoGalleryImages
    extra = 1
    verbose_name = 'Rasm'
    verbose_name_plural = "Rasmlar"
    
    def has_delete_permission(self, request, obj):
        return True

    # formfield_overrides = {
    #     models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    # }


class PhotoGalleryAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    exclude = ['title', 'created_by', 'updated_by', 'slug']
    list_display = ["slug", "title_uz", "title_ru", "title_uzb", "title_en", 'created_by']
    search_fields = ["title_uz", "title_ru", "title_uzb", "title_en"]
    inlines = [PhotoGalleryImagesAdmin]
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

        # for filename, file in request.FILES.items():
        #     if filename == "cover":
        #         continue
        #     pictures = request.FILES.getlist(filename)
        #     for picture in pictures:
        #         PhotoGalleryImages.objects.create(gallery=obj, image=picture)
        # return super(PhotoGalleryAdmin, self).save_model(request, obj, form, change)


admin.site.register(PhotoGallery, PhotoGalleryAdmin)
