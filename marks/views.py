from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import Student, Teacher, Subject
from marks.forms import CreateTeacherMarkForm, UpdateTeacherMarkForm, CreateStudentMarkForm, UpdateStudentMarkForm, \
    CreateSubjectMarkForm, UpdateSubjectMarkForm, CreateNPDMarkForm
from marks.mixins import StudentAccessMixin, TeacherAccessMixin
from marks.models import TeacherMark, StudentMark, SubjectMark, NPDMark
from npd.models import NPD


class TeacherMarkListView(ListView):
    model = TeacherMark


class TeacherMarkCreateView(CreateView, TeacherAccessMixin):
    model = TeacherMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateTeacherMarkForm

    def form_valid(self, form):
        teacher_id = self.request.POST.get('teacher_id', None)
        if teacher_id:
            form.instance.mark = Teacher.objects.filter(id=teacher_id).first()
            form.instance.who_rated = self.request.user
            return super(TeacherMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No teacher_id')


class TeacherMarkUpdateView(UpdateView):
    model = TeacherMark
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateTeacherMarkForm


class StudentMarkListView(ListView):
    model = StudentMark


class StudentMarkCreateView(CreateView, StudentAccessMixin):
    model = StudentMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateStudentMarkForm

    def form_valid(self, form):
        student_id = self.request.POST.get('student_id', None)
        if student_id:
            form.instance.mark = Student.objects.filter(id=student_id).first()
            form.instance.who_rated = self.request.user
            return super(StudentMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No student_id')


class StudentMarkUpdateView(UpdateView):
    model = StudentMark
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateStudentMarkForm


class SubjectMarkListView(ListView):
    model = SubjectMark


class SubjectMarkCreateView(CreateView):
    model = SubjectMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateSubjectMarkForm

    def form_valid(self, form):
        subject_id = self.request.POST.get('subject_id', None)
        if subject_id:
            form.instance.mark = Subject.objects.filter(id=subject_id).first()
            form.instance.who_rated = self.request.user
            return super(SubjectMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No subject_id')


class SubjectMarkUpdateView(UpdateView):
    model = SubjectMark
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateSubjectMarkForm


class NPDMarkListView(ListView):
    model = NPDMark


class NPDMarkCreateView(CreateView):
    model = NPDMark
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("home")
    form_class = CreateNPDMarkForm

    def form_valid(self, form):
        npd_id = self.request.POST.get('npd_id', None)
        if npd_id:
            form.instance.mark = NPD.objects.filter(id=npd_id).first()
            form.instance.who_rated = self.request.user
            return super(NPDMarkCreateView, self).form_valid(form)
        else:
            raise ValueError('No npd_id')


class NPDMarkUpdateView(UpdateView):
    model = NPDMark
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home")
    form_class = UpdateSubjectMarkForm

