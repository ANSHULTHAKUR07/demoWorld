# from django.contrib import admin

# # Register your models here.

# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.admin import UserAdmin as UA
# from .models import Employee
# from .forms import UserForm
# from django.contrib import admin


# class UserAdmin(UA):
#     add_form = UserForm()

#     fieldsets = (
#         (None, {"fields": ("password",)}),
#         (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password", "password"),
#             },
#         ),
#     )
#     list_display = ("email", "first_name", "last_name", "is_staff")
#     ordering = ("-is_staff",)
#     readonly_fields=('last_login', 'date_joined')



# admin.site.register(Employee, UserAdmin)
