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
        "rating"
    )
admin.site.register(models.School, SchoolAdmin)


class ScholarshipAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "link",
        "benefit"
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

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )
admin.site.register(models.Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country"
    )
admin.site.register(models.City, CityAdmin)