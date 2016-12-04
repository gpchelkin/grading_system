from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import Teacher, Student, User


class UserListView(ListView):
    model = User


class TeacherListView(ListView):
    model = Teacher
    pass


class TeacherCreateView(CreateView):
    model = Teacher
    pass


class TeacherUpdateView(UpdateView):
    model = Teacher
    pass


class StudentListView(ListView):
    model = Student
    pass


class StudentCreateView(CreateView):
    model = Student
    pass


class StudentUpdateView(UpdateView):
    model = Student
    pass

