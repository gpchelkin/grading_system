from django.contrib import admin

from marks.models import TeacherMark, StudentMark, SubjectMark, NPDMark

admin.site.register(TeacherMark)
admin.site.register(StudentMark)
admin.site.register(SubjectMark)
admin.site.register(NPDMark)
