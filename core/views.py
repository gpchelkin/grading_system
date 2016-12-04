from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.forms import CreateStudentForm, UpdateStudentForm, CreateTeacherForm, UpdateTeacherForm
from core.models import Teacher, Student, User


class UserListView(ListView):
    model = User


class TeacherListView(ListView):
    model = Teacher


class TeacherCreateView(CreateView):
    model = Teacher
    template_name_suffix = "_create_form"
    form_class = CreateTeacherForm


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name_suffix = "_update_form"
    form_class = UpdateTeacherForm


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    template_name_suffix = "_create_form"
    form_class = CreateStudentForm


class StudentUpdateView(UpdateView):
    model = Student
    template_name_suffix = "_update_form"
    form_class = UpdateStudentForm


