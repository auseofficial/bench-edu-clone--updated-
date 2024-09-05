from django.db import models
from django.contrib.auth.models import User


class Version(models.Model):
    version_code = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_versions')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.version


class Section(models.Model):
    section_code = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.section


class Session(models.Model):
    session_code = models.CharField(max_length=100)
    session = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)  # Reference by string
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.session
