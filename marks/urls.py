from django.conf.urls import url

from marks.views import TeacherMarkListView, TeacherMarkCreateView, TeacherMarkUpdateView, StudentMarkListView, \
    StudentMarkCreateView, StudentMarkUpdateView, SubjectMarkListView, SubjectMarkCreateView, SubjectMarkUpdateView

urlpatterns = [

    url(r'teacher/all/$', TeacherMarkListView.as_view(), name="all_teachers_mark"),
    url(r'teacher/add/$', TeacherMarkCreateView.as_view(), name="add_teachers_mark"),
    url(r'teacher/(?P<pk>\d+)/update/$', TeacherMarkUpdateView.as_view(), name="update_teacher_mark"),

    url(r'student/all/$', StudentMarkListView.as_view(), name="all_student_mark"),
    url(r'student/add/$', StudentMarkCreateView.as_view(), name="add_student_mark"),
    url(r'student/(?P<pk>\d+)/update/$', StudentMarkUpdateView.as_view(), name="update_student_mark"),

    url(r'subject/all/$', SubjectMarkListView.as_view(), name="all_subject_mark"),
    url(r'subject/add/$', SubjectMarkCreateView.as_view(), name="add_subject_mark"),
    url(r'subject/(?P<pk>\d+)/update/$', SubjectMarkUpdateView.as_view(), name="update_subject_mark"),
]
