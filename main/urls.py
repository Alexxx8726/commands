from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('git_commands/', views.git_commands, name='git_commands'),
    path('django_commands/', views.django_cmds, name='django_commands'),
    path('postgres_commands/', views.postgres_commands, name='postgres_commands'),
]