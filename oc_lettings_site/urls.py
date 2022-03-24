from django.contrib import admin
from django.urls import path, include

from . import views
from lettings import urls as lettings_urls
from profiles import urls as profiles_urls
from homepage import urls as homepage_urls

urlpatterns = [
    path('', include(homepage_urls, namespace='homepage')),
    path('lettings/', include(lettings_urls, namespace='lettings')),
    path('profiles/', include(profiles_urls, namespace='profiles')),
    path('admin/', admin.site.urls),
]
