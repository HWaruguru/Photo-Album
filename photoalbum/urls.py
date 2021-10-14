
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url('^$',views.index, name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)