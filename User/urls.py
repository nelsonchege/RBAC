from django.urls import path
from .views import hello_world,ListUsers,ListSubUsers
urlpatterns = [
    path('hello', hello_world),
    path('ListUsers/', ListUsers.as_view()),
    path('ListUsers/<int:pk>', ListUsers.as_view()),
    path('ListSubUsers/', ListSubUsers.as_view()),
    path('ListSubUsers/<int:pk>', ListSubUsers.as_view()),
]