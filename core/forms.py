from django import forms

from core.models import Teacher, Student


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
