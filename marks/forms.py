from django import forms
from django.forms import TextInput

from marks.models import StudentMark, TeacherMark, SubjectMark


class CreateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        exclude = ['date', 'mark']
        fields = '__all__'


class UpdateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        exclude = ['date', 'mark']
        fields = '__all__'


class CreateStudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        exclude = ['date', 'mark']
        fields = '__all__'
        widgets = {
            'teamwork_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'mutual_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'speak_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'learning_attitudes_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
        }


class UpdateStudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        exclude = ['date', 'mark']
        fields = '__all__'


class CreateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        exclude = ['date', 'mark']
        fields = '__all__'


class UpdateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        exclude = ['date', 'mark']
        fields = '__all__'
