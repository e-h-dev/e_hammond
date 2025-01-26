from django.db import models


# Create your models here.

class Contacts(models.Model):

    class Meta:
        verbose_name_plural = "Contacts"

    name = models.CharField(max_length=26)
    send_to = models.CharField(max_length=240)
    subject = models.CharField(max_length=52, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    
