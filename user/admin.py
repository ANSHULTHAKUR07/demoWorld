# from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as UA
from .models import ShoppingUser
from .forms import UserForm
from django.contrib import admin


class UserAdmin(UA):
    add_form = UserForm()

    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    ordering = ("-is_staff",)
    readonly_fields=('last_login', 'date_joined')



admin.site.register(ShoppingUser, UserAdmin)

# class MyUser(admin.ModelAdmin):
#     list_display = ("email", "first_name", "last_name", "phone_number", "state", "gender")
#     ordering = ("-is_staff",)
#     readonly_fields=('last_login', 'date_joined')


# admin.site.register(ShoppingUser, MyUser)
