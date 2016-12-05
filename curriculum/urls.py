from django.conf.urls import url

from core.views import TeacherListView, TeacherCreateView, TeacherUpdateView, StudentUpdateView, StudentListView, \
    StudentCreateView, GroupListView

urlpatterns = [

    url(r'teacher/all/$', TeacherListView.as_view(), name="all_teachers"),
    url(r'teacher/add/$', TeacherCreateView.as_view(), name="add_teacher"),
    url(r'teacher/(?P<pk>\d+)/update/$', TeacherUpdateView.as_view(), name="update_teacher"),

    url(r'student/all/(?P<group>\d+)$', StudentListView.as_view(), name="all_students"),
    url(r'student/add/$', StudentCreateView.as_view(), name="add_student"),
    url(r'student/(?P<pk>\d+)/update/$', StudentUpdateView.as_view(), name="update_student"),

    url(r'group/all/$', GroupListView.as_view(), name="all_groups"),

]

