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
    # path('user-delete/<str:pk>/', views.userDelete, name = "user-delete"),
    path('event-list/', views.eventList, name = "event-list"),
    path('attending-event-list/<str:pk>/', views.attendingList, name = "attending-event-list"),
    path('not-attending-event/<str:pk>/', views.notAttendingList, name = "not-attending-event"),
    # path('event-detail/<str:pk>/', views.eventDetail, name = "event-detail"),
    path('event-create/', views.eventCreate, name = "event-create"),
    # path('event-update/<str:pk>/', views.eventUpdate, name = "event-update"),
    # path('event-delete/<str:pk>/', views.eventDelete, name = "event-delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)