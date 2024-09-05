from django.views.generic import ListView
from .models import Session, Version, Section

class SessionListView(ListView):
    model = Session
    template_name = 'session_list.html'
    context_object_name = 'sessions'

class VersionListView(ListView):
    model = Version
    template_name = 'version_list.html'
    context_object_name = 'versions'

class SectionListView(ListView):
    model = Section
    template_name = 'section_list.html'  
    context_object_name = 'sections'