from django.conf.urls import url

from curriculum.views import ClassesTypeListView

urlpatterns = [

    url(r'classes_type/all/$', ClassesTypeListView.as_view(), name="all_classes_types"),

]

