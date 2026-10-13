from django.urls import path

from . import views

app_name = "faculty"

urlpatterns = [
    path("", views.index, name="index"),
    path("programs/", views.programs, name="programs"),
    path("programs/<int:program_id>/", views.program_detail, name="program_detail"),
    path("departments/", views.departments, name="departments"),
    path(
        "departments/<int:department_id>/",
        views.department_detail,
        name="department_detail",
    ),
    path("exchange/", views.exchange, name="exchange"),
]
