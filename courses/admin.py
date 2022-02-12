from django.contrib import admin

# Register your models here.

from . models import Lessons, Module, Courses

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'them', 'status']
    prepopulated_fields = {'slug':('them',)}

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_lessons', 'status']
    prepopulated_fields = {'slug':('module_name',)}



@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'get_modules', 'status']
    prepopulated_fields = {'slug':('course_name',)}
    # def get_modules(self, obj):
    #     return "\n".join([p.them for p in obj.modules.all()])
