from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.





class CustomUser(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number')