from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from django.contrib.auth.models import User
from profile.models import Profile

import secrets

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)


class ProfileInline(StackedInline):
    model = Profile
    #readonly_fields = ('api_token',)
    ordering_field = 'user'
    fields = ['licence_id', 'licence_notes', 'api_token']
    can_delete = False
    extra = 1

    def save_model(self, request, obj, form, change):
        # Pass the request into the model's save() method.
        obj.save(request=request)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    inlines = [ProfileInline]
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    # Override fieldsets to remove permissions
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save(request=request)
        formset.save_m2m()

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass