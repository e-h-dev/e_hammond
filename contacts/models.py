from django.db import models


# Create your models here.

class Contacts(models.Model):

    class Meta:
        verbose_name_plural = "Contacts"

    name = models.CharField(max_length=26)
    send_to = models.CharField(max_length=240)
    subject = models.CharField(max_length=52, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=25, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    has_reply = models.BooleanField(default=False)
    new_reply = models.BooleanField(default=False)


class Replied(models.Model):

    class Meta:
        verbose_name_plural = "Replies"

    thread = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    name = models.CharField(max_length=26, null=True, blank=True)
    send_to = models.CharField(max_length=240)
    subject = models.CharField(max_length=52, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
