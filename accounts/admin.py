from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django_summernote.models import Attachment
admin.site.unregister(Attachment)

from .forms import UserAdminCreationForm, UserAdminChangeForm
User = get_user_model()

Group._meta.verbose_name = 'Рол'
Group._meta.verbose_name_plural = 'Роллар'


class UserAdmin(UserAdmin):
    list_display = ['username', 'firstname', 'lastname', 'role']
    search_fields = ['username', 'firstname', 'lastname', 'email']
    list_filter = ['role']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'firstname', 'lastname', 'role')}),

    )
    # add_fieldsets = None
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password',)}
        ),
    )

admin.site.register(User, UserAdmin)
