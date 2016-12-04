from django.contrib import admin

from marks.models import TeacherMark, StudentMark, SubjectMark

admin.site.register(TeacherMark)
admin.site.register(StudentMark)
admin.site.register(SubjectMark)
