from django.contrib import admin
from tinymce.widgets import TinyMCE
from django import forms

from exhibit.models import ExhibitImages, Exhibit, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'index')
    exclude = ('slug', 'created_by', 'updated_by', 'name')
    search_fields = ('name_uz', 'name_uzb', 'name_ru', 'name_en',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class ExhibitImagesAdmin(admin.TabularInline):
    model = ExhibitImages
    extra = 3

    def has_delete_permission(self, request, obj=None):
        return True


class ExhibitForm(forms.ModelForm):
    body_uz = forms.CharField(label='Экспонат ҳақида:  [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    body_uzb = forms.CharField(label='Экспонат ҳақида:  [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    body_ru = forms.CharField(label='Экспонат ҳақида:  [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    body_en = forms.CharField(label='Экспонат ҳақида:  [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    summary_uz = forms.CharField(label='Қисқача мазмуни [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    summary_uzb = forms.CharField(label='Қисқача мазмуни [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    summary_ru = forms.CharField(label='Қисқача мазмуни [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    summary_en = forms.CharField(label='Қисқача мазмуни [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = Exhibit
        exclude = (
            'slug',
            'created_by',
            'updated_by',
            'name',
            'summary',
            'used_years',
            'body',
            'audio',
        )

class ExhibitAdmin(admin.ModelAdmin):
    form = ExhibitForm
    inlines = [ExhibitImagesAdmin]
    list_display = ('slug', 'name', 'summary', 'cover', 'created_at', 'to_main_page', 'to_about_page')
    search_fields = ['name_uz', 'name_uzb', 'name_ru', 'name_en',
                     'category__name_uz', 'category__name_uzb', 'category__name_ru', 'category__name_en']
    list_filter = ('category__name_uz', 'category__name_uzb', 'category__name_ru', 'category__name_en',)
    exclude = (
        'slug',
        'created_by',
        'updated_by',
        'name',
        'summary',
        'used_years',
        'body',
        'audio',
    )
    actions = ['delete_selected']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated = request.user
        return super(ExhibitAdmin, self).save_model(request, obj, form, change)

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "Ўчириш"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
