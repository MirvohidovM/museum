from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    search_fields = ['name_uz', 'name_uzb', 'name_ru', 'name_en', ]
    list_display = ['name_uz', 'name_uzb', 'name_ru', 'name_en', 'index']
    exclude = (
        'slug',
        'name',
        'position',
        'created_by',
        'updated_by',
    )

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "Ўчириш"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Employee, EmployeeAdmin)
