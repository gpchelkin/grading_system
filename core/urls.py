from django.conf.urls import url

from core.views import TeacherListView, TeacherCreateView, TeacherUpdateView, StudentUpdateView, StudentListView, \
    StudentCreateView

urlpatterns = [
    url(r'teacher/(?P<pk>\d+)/update/$', TeacherUpdateView.as_view()),
    url(r'teacher/all/$', TeacherListView.as_view()),
    url(r'teacher/add/$', TeacherCreateView.as_view()),

    url(r'student/(?P<pk>\d+)/update/$', StudentUpdateView.as_view()),
    url(r'student/all/$', StudentListView.as_view()),
    url(r'student/add/$', StudentCreateView.as_view()),
]
