from django.db import models

    

class Reviews(models.Model):
    class Meta:
        verbose_name_plural = "Reviews"


    name = models.CharField(max_length=254)
    rating = models.IntegerField(default=1,
                                 choices=((i, i) for i in range(1, 6)))
    review = models.TextField(max_length=600, null=True, blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)