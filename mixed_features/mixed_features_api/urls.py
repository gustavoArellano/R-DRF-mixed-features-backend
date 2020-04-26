from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('user-list/', views.userList, name = "user-list"),
    # path('user-detail/<str:pk>/', views.userDetail, name = "user-detial"),
    path('user-signup/', views.signUp, name = "user-signup"),
    # path('user-update/<str:pk>/', views.userUpdate, name = "user-update"),
    # path('user-delete/<str:pk>/', views.userDelete, name = "user-delete")
]