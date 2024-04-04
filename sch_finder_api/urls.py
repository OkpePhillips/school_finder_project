from django.urls import path
from . import views

# import for swagger documentation
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("register/", views.RegisterUserApi.as_view(), name="register"),
    path("login/", views.LoginApi.as_view(), name="login"),
    path("me/", views.UserApi.as_view(), name="profile"),
    path("me/", views.UserApi.as_view(), name="profile_update"),
    path("me/", views.UserApi.as_view(), name="profile_delete"),
    path("logout/", views.LogoutApi.as_view(), name="logout"),
    path("school/", views.SchoolApi.as_view(), name="create_sch"),
    path("schools/", views.GetSchoolApi.as_view(), name="get_sch"),
    path("schools/<int:id>/", views.GetSchoolApi.as_view(), name="get_specific_sch"),
    path('school/<int:id>/', views.SchoolApi.as_view(), name='delete_school'),
    path('school/<int:id>/', views.SchoolApi.as_view(), name='edit_school'),
    path("scholarship/", views.ScholarshipApi.as_view(), name="create_scholarship"),
    path("scholarships/", views.ScholarshipGetApi.as_view(), name="get_scholarship"),
    path("scholarships/<int:id>/", views.ScholarshipApi.as_view(), name="get_specific_scholarship"),
    path("scholarship/<int:id>/", views.ScholarshipGetApi.as_view(), name="update_scholarship"),
    path("scholarship/<int:id>/", views.ScholarshipApi.as_view(), name="delete_scholarship"),
    path("change_password/",views.ChangePassword.as_view(), name="change_password"),
    path("review/", views.ReviewApi.as_view(), name="create_review"),
    path("reviews/", views.ReviewGetApi.as_view(), name="get_reviews"),
    path("review/<int:id>/", views.ReviewApi.as_view(), name="update_review"),
    path("reviews/<int:id>/", views.ReviewGetApi.as_view(), name="get_school_review"),
    path("review/<int:id>/", views.ReviewApi.as_view(), name="delete_review"),
    path("country/", views.CountryApi.as_view(), name="create_country"),
    path("countries/", views.GetCountryApi.as_view(), name="get_country"),
    path("countries/<int:id>/", views.GetCountryApi.as_view(), name="get_country"),
    path("city/", views.CityApi.as_view(), name="create_city"),
    path("cities/", views.GetCitiesApi.as_view(), name="get_city"),
    path("city/<int:id>/", views.GetCitiesApi.as_view(), name="get_city"),
]

