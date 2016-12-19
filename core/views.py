from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from core.forms import CreateStudentForm, UpdateStudentForm, CreateTeacherForm, UpdateTeacherForm, UpdateSubjectForm, \
    CreateSubjectForm
from core.models import Teacher, Student, User, Group, Subject
# from marks.forms import CreateStudentMarkForm, CreateTeacherMarkForm, CreateSubjectMarkForm


class MainPageTemplateView(TemplateView):
    template_name = 'core/main_page.html'


class GroupListView(ListView):
    model = Group


class UserListView(ListView):
    model = User


class TeacherListView(ListView):
    model = Teacher

    def get_context_data(self, **kwargs):
        data = super(TeacherListView, self).get_context_data()
        # form = CreateTeacherMarkForm()
        # data.update({'form': form})
        return data


class TeacherCreateView(CreateView):
    model = Teacher
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateTeacherForm


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateTeacherForm


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        group_number = self.kwargs.get('group')
        qs = super(StudentListView, self).get_queryset()
        return qs.filter(user_group_full_name__id=group_number)

    def get_context_data(self, **kwargs):
        data = super(StudentListView, self).get_context_data()
        # form = CreateStudentMarkForm()
        # data.update({'form': form})
        return data


class StudentCreateView(CreateView):
    model = Student
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateStudentForm


class StudentUpdateView(UpdateView):
    model = Student
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateStudentForm


class SubjectListView(ListView):
    model = Subject

    def get_queryset(self):
        type_number = self.kwargs.get('type')
        qs = super(SubjectListView, self).get_queryset()
        return qs.filter(subject_type__id=type_number)

    def get_context_data(self, **kwargs):
        data = super(SubjectListView, self).get_context_data()
        # form = CreateSubjectMarkForm()
        # data.update({'form': form})
        return data


class SubjectCreateView(CreateView):
    model = Subject
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = UpdateSubjectForm


class SubjectUpdateView(UpdateView):
    model = Subject
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateSubjectForm


