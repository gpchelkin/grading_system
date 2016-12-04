from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import Student, Teacher
from marks.forms import CreateTeacherMarkForm, UpdateTeacherMarkForm, CreateStudentMarkForm, UpdateStudentMarkForm, \
    CreateSubjectMarkForm, UpdateSubjectMarkForm
from marks.mixins import StudentAccessMixin, TeacherAccessMixin
from marks.models import TeacherMark, StudentMark, SubjectMark


class TeacherMarkListView(ListView):
    model = TeacherMark


class TeacherMarkCreateView(CreateView):
    model = TeacherMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateTeacherMarkForm

    def form_valid(self, form):
        teacher_id = self.request.POST.get('teacher_id', None)
        if teacher_id:
            form.instance.mark = Teacher.objects.filter(id=teacher_id).first()
            return super(TeacherMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No teacher_id')


class TeacherMarkUpdateView(UpdateView):
    model = TeacherMark
    template_name_suffix = "_update_form"
    form_class = UpdateTeacherMarkForm


class StudentMarkListView(ListView):
    model = StudentMark


class StudentMarkCreateView(CreateView):
    model = StudentMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateStudentMarkForm

    def form_valid(self, form):
        student_id = self.request.POST.get('student_id', None)
        if student_id:
            form.instance.mark = Student.objects.filter(id=student_id).first()
            return super(StudentMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No student_id')


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

