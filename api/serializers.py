from .models import *
from rest_framework import serializers, status
from rest_framework.response import Response

class UserSerializer(serializers.HyperlinkedModelSerializer):
    permission = serializers.CharField(source='permission_id')
    
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_password = validated_data.get('user_password', instance.user_password)
        instance.user_full_name = validated_data.get('user_full_name', instance.user_full_name)
        instance.user_title = validated_data.get('user_title', instance.user_title)
        instance.user_mobile_1 = validated_data.get('user_mobile_1', instance.user_mobile_1)
        instance.user_mobile_2 = validated_data.get('user_mobile_2', instance.user_mobile_2)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_active = validated_data.get('user_active', instance.user_active)
        instance.permission = validated_data.get('permission', instance.permission)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    permission = serializers.CharField(source='permission_id')
    
    class Meta:
        model = Project
        fields = '__all__'
        
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.status = validated_data.get('status', instance.status)
        instance.permission = validated_data.get('permission', instance.permission)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.CharField(source='project_id')
    assigned_user = serializers.CharField(source='assigned_user_id')
    
    class Meta:
        model = Task
        fields = '__all__'
        
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.project = validated_data.get('project', instance.project)
        instance.assigned_user = validated_data.get('assigned_user', instance.assigned_user)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField()
