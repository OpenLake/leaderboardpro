from django.urls import path
from .views import  AddUserView,CFUsersView

urlpatterns = [
    path('addCFuser', AddUserView.as_view()),
    path('getCFusers',CFUsersView.as_view()),
]