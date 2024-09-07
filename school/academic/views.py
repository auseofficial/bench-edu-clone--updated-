from django.views.generic import ListView
from .models import Session, Version, Section, Subject

class SessionListView(ListView):
    model = Session
    context_object_name = 'sessions'

class VersionListView(ListView):
    model = Version
    context_object_name = 'versions'

class SectionListView(ListView):
    model = Section
    context_object_name = 'sections'

class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'subjects_list.html'
