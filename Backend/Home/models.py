from django.db import models
from phone_field import PhoneField


# Create your models here.

class User(models.Model):
    name  = models.CharField(max_length=225, null=True, blank=True)
    dob   = models.DateField(auto_now=False)
    email = models.EmailField(max_length=225, null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return str(self.name)