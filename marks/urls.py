from django.conf.urls import url

from marks.views import TeacherMarkListView, TeacherMarkCreateView, TeacherMarkUpdateView, StudentMarkListView, \
    StudentMarkCreateView, StudentMarkUpdateView, SubjectMarkListView, SubjectMarkCreateView, SubjectMarkUpdateView

urlpatterns = [

    url(r'teacher/all/$', TeacherMarkListView.as_view()),
    url(r'teacher/add/$', TeacherMarkCreateView.as_view()),
    url(r'teacher/(?P<pk>\d+)/update/$', TeacherMarkUpdateView.as_view()),



    url(r'student/all/$', StudentMarkListView.as_view()),
    url(r'student/add/$', StudentMarkCreateView.as_view()),
    url(r'student/(?P<pk>\d+)/update/$', StudentMarkUpdateView.as_view()),


    url(r'subject/all/$', SubjectMarkListView.as_view()),
    url(r'subject/add/$', SubjectMarkCreateView.as_view()),
    url(r'subject/(?P<pk>\d+)/update/$', SubjectMarkUpdateView.as_view()),
]
