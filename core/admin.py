from django.contrib import admin

from core.models import User, Student, Teacher, Subject, Group

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)

