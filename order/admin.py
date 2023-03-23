from django.contrib import admin

from .models import Order, ExcursionType


class ExcursionTypeAdmin(admin.ModelAdmin):
    exclude = ['name']


class OrderAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by', 'slug', 'firstname', 'lastname', 'organization', 'status', 'reason',)
    list_display = ('lastname_uz', 'lastname_uzb', 'lastname_ru', 'lastname_en',
                    'organization_uz', 'organization_uzb', 'organization_ru', 'organization_en',
                    'phone', 'visit_time', 'num_visitors', 'status')
    search_fields = ('lastname_uz', 'lastname_uzb', 'lastname_ru', 'lastname_en',
                     'organization_uz', 'organization_uzb', 'organization_ru', 'organization_en', )
    list_filter = ('status',)

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    actions = [delete_selected]
    delete_selected.short_description = 'Ўчириш'

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if 'accept' in request.POST.keys():
            obj.status = 2
        elif 'reject' in request.POST.keys():
            obj.status = 3
            obj.reason = request.POST['reason']

        return super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):

        if object_id:
            application = Order.objects.get(pk=object_id)
            if not extra_context:
                extra_context = dict()
            if application.status == 1:
                extra_context['new'] = True
            # if application.status == 2:
            #     extra_context['accepted'] = True

        return super(OrderAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)


admin.site.register(ExcursionType, ExcursionTypeAdmin)
admin.site.register(Order, OrderAdmin)
