from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from marks.models import TeacherMark, StudentMark, SubjectMark


class TeacherMarkListView(ListView):
    model = TeacherMark


class TeacherMarkCreateView(CreateView):
    model = TeacherMark


class TeacherMarkUpdateView(UpdateView):
    model = TeacherMark


class StudentMarkListView(ListView):
    model = StudentMark


class StudentMarkCreateView(CreateView):
    model = StudentMark


class StudentMarkUpdateView(UpdateView):
    model = StudentMark


class SubjectMarkListView(ListView):
    model = SubjectMark


class SubjectMarkCreateView(CreateView):
    model = SubjectMark


class SubjectMarkUpdateView(UpdateView):
    model = SubjectMark

