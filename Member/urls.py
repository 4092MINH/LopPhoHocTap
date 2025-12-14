from django.urls import path
from . import views
urlpatterns = [
    path('', views.member_index, name='member_index'),
    path('details/<slug:slug>/', views.member_detail, name='member_detail'),
]