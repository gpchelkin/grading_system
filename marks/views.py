from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import Student
from marks.forms import CreateTeacherMarkForm, UpdateTeacherMarkForm, CreateStudentMarkForm, UpdateStudentMarkForm, \
    CreateSubjectMarkForm, UpdateSubjectMarkForm
from marks.mixins import StudentAccessMixin, TeacherAccessMixin
from marks.models import TeacherMark, StudentMark, SubjectMark


class TeacherMarkListView(ListView):
    model = TeacherMark


class TeacherMarkCreateView(CreateView, TeacherAccessMixin):
    model = TeacherMark
    template_name_suffix = "_create_form"
    form_class = CreateTeacherMarkForm


class TeacherMarkUpdateView(UpdateView, TeacherAccessMixin):
    model = TeacherMark
    template_name_suffix = "_update_form"
    form_class = UpdateTeacherMarkForm


class StudentMarkListView(ListView):
    model = StudentMark


class StudentMarkCreateView(CreateView, StudentAccessMixin):
    model = StudentMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateStudentMarkForm

    def form_valid(self, form):
        form.instance.mark = self.student
        return super(StudentMarkCreateView, self).form_valid(form)


class StudentMarkUpdateView(UpdateView, StudentAccessMixin):
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

