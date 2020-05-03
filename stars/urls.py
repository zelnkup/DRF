from django.urls import path
from . import views

app_name = 'stars'

urlpatterns= [
    path('stars', views.StarListView.as_view()),
    path('stars/<slug:slug>', views.StarDetailView.as_view()),
]