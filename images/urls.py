from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views.index, name="images_index"),
    re_path(r'^search/',views.search_results,name="search_results"),
    re_path(r'^loction/',views.filter_location,name="filter-location"),
    re_path(r'^image/(\d+)',views.single_image,name ='single_image')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
