from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view()),
    path("<int:pk>", views.GetUserById.as_view())
]
