from django.urls import path
from .views import TeacherView, TeacherDetailView

urlpatterns = [
    path('assignments/', TeacherView.as_view(), name='teachers-assignments'),
    path('assignments/<int:pk>/', TeacherDetailView.as_view(), name='teachers-assignments-details')
]
