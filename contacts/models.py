from django.db import models

# Create your models here.

class Contacts(models.Model):

    class Meta:
        verbose_name_plural = "Contacts"

    name = models.CharField(max_length=26)
    subject = models.CharField(max_length=52, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    new_message = models.BooleanField(default=True)


    
