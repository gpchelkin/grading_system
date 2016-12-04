from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from marks.forms import CreateTeacherMarkForm, UpdateTeacherMarkForm, CreateStudentMarkForm, UpdateStudentMarkForm, \
    CreateSubjectMarkForm, UpdateSubjectMarkForm
from marks.models import TeacherMark, StudentMark, SubjectMark


class TeacherMarkListView(ListView):
    model = TeacherMark


class TeacherMarkCreateView(CreateView):
    model = TeacherMark
    template_name_suffix = "_create_form"
    form_class = CreateTeacherMarkForm


class TeacherMarkUpdateView(UpdateView):
    model = TeacherMark
    template_name_suffix = "_update_form"
    form_class = UpdateTeacherMarkForm


class StudentMarkListView(ListView):
    model = StudentMark


class StudentMarkCreateView(CreateView):
    model = StudentMark
    template_name_suffix = "_create_form"
    form_class = CreateStudentMarkForm


class StudentMarkUpdateView(UpdateView):
    model = StudentMark
    template_name_suffix = "_update_form"
    form_class = UpdateStudentMarkForm


class SubjectMarkListView(ListView):
    model = SubjectMark


class SubjectMarkCreateView(CreateView):
    model = SubjectMark
    template_name_suffix = "_create_form"
    form_class = CreateSubjectMarkForm


class SubjectMarkUpdateView(UpdateView):
    model = SubjectMark
    template_name_suffix = "_update_form"
    form_class = UpdateSubjectMarkForm

