from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from django.contrib.auth.models import User
from profile.models import Profile

import secrets

class ProfileInline(StackedInline):
    model = Profile
    readonly_fields = ('api_token',)
    ordering_field = 'user'
    fields = ['licence_id', 'licence_notes', 'api_token']
    can_delete = False
    extra = 1

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    inlines = [ProfileInline]
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    # fieldsets = [
    #     (None, {"fields": ["username", "email", "password"]}),
    # ]


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass