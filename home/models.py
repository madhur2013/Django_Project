from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    #date=models.models.DateField(_(""), auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name
class Services(models.Model):
    name=models.CharField(max_length=122)
    def __str__(self):
        return self.name
    