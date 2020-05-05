from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mixed_features_api.urls')),
    path('token-auth/', obtain_jwt_token), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
