from django.urls import path 
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('user-signup/', views.UserList.as_view()),
    path('current-user/', views.current_user),
    path('user-list/', views.userList, name = "user-list"),
    path('user-detail/<str:pk>/', views.userDetail, name = "user-detail"),
    path('user-update/<str:pk>/', views.userUpdate, name = "user-update"),
    # path('user-delete/<str:pk>/', views.userDelete, name = "user-delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)