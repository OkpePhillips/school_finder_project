from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterUserApi.as_view(), name="register"),
    path("login/", views.LoginApi.as_view(), name="login"),
    path("me/", views.UserApi.as_view(), name="profile"),
    path("me/", views.UserApi.as_view(), name="profile_update"),
    path("me/", views.UserApi.as_view(), name="profile_delete"),
    path("logout/", views.LogoutApi.as_view(), name="logout"),
    path("schools/", views.SchoolApi.as_view(), name="create_sch"),
    path("schools/", views.SchoolApi.as_view(), name="get_sch"),
    path('schools/<int:id>/', views.SchoolApi.as_view(), name='delete_school'),
    path('schools/<int:id>/', views.SchoolApi.as_view(), name='edit_school'),
    path("scholarships/", views.ScholarshipApi.as_view(), name="create_scholarship"),
    path("scholarships/", views.ScholarshipApi.as_view(), name="get_scholarship"),
    path("scholarships/<int:id>/", views.ScholarshipApi.as_view(), name="update_scholarship"),
    path("scholarships/", views.ScholarshipApi.as_view(), name="delete_scholarship"),
    path("change_password/",views.ChangePassword.as_view(), name="change_password"),

]