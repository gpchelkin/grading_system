from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from core.views import MainPageTemplateView
from grading_system import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mark/', include('marks.urls', 'marks')),
    url(r'^core/', include('core.urls', 'core')),
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', MainPageTemplateView.as_view(), name='home'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
