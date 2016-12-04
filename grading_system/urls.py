from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mark/', include('marks.urls', 'marls')),
    url(r'^core/', include('core.urls', 'core')),
]
