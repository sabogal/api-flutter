from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from login.api.views.views_login import *

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v1',
      description="Documentacion de las rutas del proyecto de grado",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
    #Users
   path('user/', include('login.api.routers.routers')),
    # swagger
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # login
   path('login/', Login.as_view(), name='login'),
    # logout
   path('logout/', Logout.as_view(), name='logout'),
]
