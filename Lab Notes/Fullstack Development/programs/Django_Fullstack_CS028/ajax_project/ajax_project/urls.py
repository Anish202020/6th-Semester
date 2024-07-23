from django.urls import include, path
from django.contrib import admin
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('ajax_app.urls')),   # To make post app available at /
   ]