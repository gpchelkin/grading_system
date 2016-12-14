from django import forms
from django.forms import TextInput

from marks.models import StudentMark, TeacherMark, SubjectMark, NPDMark
from npd.models import NPD

EXCLUDE_FIELDS = ['who_rated', 'date', 'mark', 'type_rated', 'what_subject', 'what_npd']


class CreateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'
        widgets = {
            'speaker_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'professionalism_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'exactingness_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'understanding_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'charisma_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'collective_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
        }


class UpdateTeacherMarkForm(forms.ModelForm):
    class Meta:
        model = TeacherMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class CreateStudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        exclude = EXCLUDE_FIELDS
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
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class CreateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'
        widgets = {
            'relevance_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'availability_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'thrill_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'fixation_material_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'learning_material_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
            'learning_organization_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'}),
        }


class UpdateSubjectMarkForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class CreateNPDMarkForm(forms.ModelForm):
    class Meta:
        model = NPDMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'
        widgets = {
            'difficult_points': TextInput(attrs={'placeholder': '1-10', 'type': 'number'})
        }


class UpdateNPDMarkForm(forms.ModelForm):
    class Meta:
        model = NPDMark
        exclude = ['date', 'mark']
        fields = '__all__'
