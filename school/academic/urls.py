from django.urls import path
from .views import SessionListView, VersionListView, SectionListView, SubjectListView

urlpatterns = [
    path('sessions/', SessionListView.as_view(), name='session-list'),
    path('versions/', VersionListView.as_view(), name='version-list'),
    path('sections/', SectionListView.as_view(), name='section-list'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),  # Updated for SubjectListView
]
