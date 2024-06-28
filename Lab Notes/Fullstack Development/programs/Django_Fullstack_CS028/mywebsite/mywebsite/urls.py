from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('pages.urls')), # Include the URLs from the pages app
]
