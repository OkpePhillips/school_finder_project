from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email"
    )

admin.site.register(models.User, UserAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "email",
        "website",
        "phone_number"
    )
admin.site.register(models.School, SchoolAdmin)

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "benefit",
        "requirement",
        "link"
    )
admin.site.register(models.Scholarship, ScholarshipAdmin)