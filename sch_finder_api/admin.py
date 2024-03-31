from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "current_degree",
        "gender",
        "nationality",
        "dob"
    )

admin.site.register(models.User, UserAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "degrees",
        "website",
        "money",
        "rating"
    )
admin.site.register(models.School, SchoolAdmin)


class ScholarshipAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "benefit",
        "link",
        "school"
    )
admin.site.register(models.Scholarship, ScholarshipAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "school_id",
        "user_id",
        "description",
        "rating"
    )
admin.site.register(models.Review, ReviewAdmin)