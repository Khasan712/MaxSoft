from distutils.command.upload import upload
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
# Create your models here.


class Lessons(models.Model):
    lesson_mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='lesson_mentor',
        on_delete=models.CASCADE
    )
    them = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    video = models.FileField(upload_to='module/vidoes')
    text = RichTextUploadingField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.them



class Module(models.Model):
    module_mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='module_mentor',
        on_delete=models.CASCADE,
    )
    module_name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    lessons = models.ManyToManyField(Lessons, related_name='lessons')
    status = models.BooleanField(default=True)

    def get_lessons(self):
        return "\n".join([p.them for p in self.lessons.all()])

    def __str__(self):
        return self.module_name


class Courses(models.Model):
    course_mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='course_mentor',
        on_delete=models.CASCADE
    )
    course_avatar = models.ImageField(upload_to='courses/avatar', blank=True)
    course_name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    modules = models.ManyToManyField(Module, related_name='modules')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

    def get_modules(self):
        return "\n".join([p.module_name for p in self.modules.all()])

    @property
    def get_course_avatar(self):
        if self.course_avatar and hasattr(self.course_avatar, 'url'):
                return self.course_avatar.url
        else:
            return "/media/courses/default_avatar/defaut_avatar.jpg"