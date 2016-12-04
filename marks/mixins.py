from django.core.exceptions import PermissionDenied
from django.views import View

from core.models import Student, Teacher


class StudentAccessMixin(View):
    def dispatch(self, request, *args, **kwargs):
        student = Student.objects.filter(user_connection__id=request.user.pk).first()
        if not student:
            raise PermissionDenied
        else:
            self.student = student
            return super(StudentAccessMixin, self).dispatch(request, *args, **kwargs)


class TeacherAccessMixin(View):
    def dispatch(self, request, *args, **kwargs):
        teacher = Teacher.objects.filter(user_connection__id=request.user.pk).first()
        if not teacher:
            raise PermissionDenied
        else:
            self.teacher = teacher
            return super(TeacherAccessMixin, self).dispatch(request, *args, **kwargs)
