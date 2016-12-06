from django.conf.urls import url
from reports.views import suka_peredelay_eto_zaglushka

urlpatterns = [

    url(r'student/(?P<pk>\d+)/marks/all/$', suka_peredelay_eto_zaglushka, name="student_marks_report"),
    url(r'student/(?P<pk>\d+)/marks/period/$', suka_peredelay_eto_zaglushka, name="student_marks_report_period"),

    url(r'teacher/(?P<pk>\d+)/marks/all/$', suka_peredelay_eto_zaglushka, name="teacher_marks_report"),
    url(r'teacher/(?P<pk>\d+)/marks/period/$', suka_peredelay_eto_zaglushka, name="student_marks_report_period"),

    url(r'subject/(?P<pk>\d+)/$', suka_peredelay_eto_zaglushka, name="subject_report"),

    url(r'curriculum/(?P<type>\d+)/$', suka_peredelay_eto_zaglushka, name="curriculum_report"),

    url(r'npd/(?P<type>\d+)/student/(?P<pk>\d+)/$', suka_peredelay_eto_zaglushka, name="npd_by_student_report"),

    url(r'marks/user/$', suka_peredelay_eto_zaglushka, name="my_marks_report"),

    url(r'students/all/$', suka_peredelay_eto_zaglushka, name="students_all_report"),
    url(r'teachers/all/$', suka_peredelay_eto_zaglushka, name="teachers_all_report"),


]

