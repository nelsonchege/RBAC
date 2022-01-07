from django.urls import path
from .views import hello_world,ListUsers,ListSubUsers
urlpatterns = [
    path('hello', hello_world),
    # used to get and post a new mainuser into db
    path('ListUsers/', ListUsers.as_view()),
    # used to get a specific main user to update or delete
    path('ListUsers/<int:pk>', ListUsers.as_view()),
    # used to post a new subuser into db
    path('ListSubUsers/', ListSubUsers.as_view()),
    # used to get a specific subusers for a main user using the mainusers_id
    path('ListSubUsers/<int:pk>', ListSubUsers.as_view()),
]