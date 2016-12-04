from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import Teacher, Student, User


class UserListView(ListView):
    model = User


class TeacherListView(ListView):
    model = Teacher


class TeacherCreateView(CreateView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    pass


