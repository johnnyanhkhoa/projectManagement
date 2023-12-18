from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import *
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *

# Create your views here.
'''User'''
def users_service(request):
    users = User.objects.all()
    users_list = list(users.values())
    
    return JsonResponse(users_list, safe=False)

def user_service(request,pk):
    users = User.objects.filter(pk=pk)
    users_list = list(users.values()[0])
    
    return JsonResponse(users_list, safe=False)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser] # Read / Write
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read only
    

'''Project'''
def projects_service(request):
    projects = Project.objects.all()
    projects_list = list(projects.values())
    
    return JsonResponse(projects_list, safe=False)

def project_service(request,pk):
    projects = Project.objects.filter(pk=pk)
    projects_list = list(projects.values()[0])
    
    return JsonResponse(projects_list, safe=False)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAdminUser] # Read / Write
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read only
    

'''Task'''
def tasks_service(request):
    tasks = Task.objects.all()
    tasks_list = list(tasks.values())
    
    return JsonResponse(tasks_list, safe=False)

def task_service(request,pk):
    tasks = Task.objects.filter(pk=pk)
    tasks_list = list(tasks.values()[0])
    
    return JsonResponse(tasks_list, safe=False)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAdminUser] # Read / Write
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read only
    

class TestAPIView(APIView):
    
    def get(self, request):
        return Response('oke')
    
    def post(self, request):
        da = InfoSerializer(data=request.data)
        if not da.is_valid():
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
        
        print(da.data)
        return Response('oke, data received sucessfully')
    


    
    
    


    
