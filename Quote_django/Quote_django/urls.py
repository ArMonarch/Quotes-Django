from django.contrib import admin
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('', include("core.urls")),
    path('Quote/', include('Quote.urls')),
    path('admin/', admin.site.urls),
]
