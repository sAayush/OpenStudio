from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/accounts/', include('accounts.urls')),
    path('stats/posts/', include('post.urls')),
    path('stats/stats/', include('stats.urls')),
]
