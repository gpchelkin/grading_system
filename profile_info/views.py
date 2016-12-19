from django.views.generic import ListView
from django.views.generic import TemplateView

from marks.models import StudentMark
from marks.models import TeacherMark, SubjectMark


class ProfileTemplateView(TemplateView):
    template_name = "profile_info/main.html"


class ProfileMyMarksTemplateView(TemplateView):
    template_name = "profile_info/my_marks.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileMyMarksTemplateView, self).get_context_data(**kwargs)
        teachers_marks = TeacherMark.objects.filter(who_rated=self.request.user)
        student_marks = StudentMark.objects.filter(who_rated=self.request.user)
        subject_marks = SubjectMark.objects.filter(who_rated=self.request.user)
        context.update({
            'teachers_marks': teachers_marks,
            'student_marks': student_marks,
            'subject_marks': subject_marks
        })
        return context


class ProfileMarksForMeTemplateView(TemplateView):
    template_name = "profile_info/for_me_marks.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileMarksForMeTemplateView, self).get_context_data(**kwargs)
        if self.request.user.is_student:
            student_marks = StudentMark.objects.filter(mark__user_connection=self.request.user)
            context.update({
                'student_marks': student_marks,
            })
        elif self.request.user.is_teacher:
            teachers_marks = TeacherMark.objects.filter(mark__user_connection=self.request.user)
            context.update({
                'teachers_marks': teachers_marks,
            })
        return context


