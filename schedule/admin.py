from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'image')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)