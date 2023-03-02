from django.urls import path
from .views import TeachersViews, TeachersCreateView, TeachersUpdateView, TeachersDeleteView, TeacherViews

app_name = 'teachers'


urlpatterns = [
    path("", TeachersViews.as_view(), name="teachers_list"),
    # path("<int:pk>/", TeacherViews.as_view(), name="teacher_view"),
    path("create/", TeachersCreateView.as_view(), name="teachers_create"),
    path("<int:pk>/update/", TeachersUpdateView.as_view(), name="teachers_update"),
    path("<int:pk>/delete/", TeachersDeleteView.as_view(), name="teachers_delete"),
]
