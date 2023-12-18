from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

'''User'''
class Permission(models.Model):
    permission = models.CharField(max_length=10, blank=False, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.permission


class User(models.Model):
    user_email = models.EmailField(max_length=50, blank=False)
    user_password = models.CharField(max_length=100, blank=False)
    user_active = models.CharField(max_length=10)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, blank=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.user_email



'''Project'''
class Project(models.Model):
    project_name = models.CharField(max_length=255, blank=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, blank=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.project_name
    

'''Task'''
class Task(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, blank=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title