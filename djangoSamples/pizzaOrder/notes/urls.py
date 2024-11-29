"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.NotesListView.as_view() , name="notes.list"),
    path ('<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path ('<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.edit"),
    path ('<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path ('new', views.NotesCreateView.as_view(), name="notes.new"),
]
