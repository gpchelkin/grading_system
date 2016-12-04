from django import forms
from marks.models import StudentMark, TeacherMark, SubjectMark


class CreateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        fields = '__all__'


class UpdateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        fields = '__all__'


class CreateStudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        fields = '__all__'


class UpdateStudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        fields = '__all__'


class CreateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        fields = '__all__'


class UpdateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        fields = '__all__'
