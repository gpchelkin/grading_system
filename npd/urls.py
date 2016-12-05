from django.conf.urls import url

from npd.views import NPDListView

urlpatterns = [

    url(r'npd/all/$', NPDListView.as_view(), name="all_npd"),

]
