from django.conf.urls import url

from core.views import MainPageTemplateView
urlpatterns = [
    url(r'^$', MainPageTemplateView.as_view(), name='home'),

]

# from npd.views import NPDListView
#
# urlpatterns = [
#
#     url(r'npd/all/$', NPDListView.as_view(), name="all_npd"),
#
# ]
