from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('', homepage),
]
