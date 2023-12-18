from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
urlpatterns = [
    path('user-service/', views.users_service, name='users_service'),
    path('user-service/<int:pk>/', views.user_service, name='user_service'),
    
    path('project-service/', views.projects_service, name='projects_service'),
    path('project-service/<int:pk>/', views.project_service, name='project_service'),
    
    path('task-service/', views.tasks_service, name='tasks_service'),
    path('task-service/<int:pk>/', views.task_service, name='task_service'),
    
    

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('info/', TestAPIView.as_view()),
    
    
    
]

