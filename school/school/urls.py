from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "School Management System "

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academic/', include('academic.urls')),
]