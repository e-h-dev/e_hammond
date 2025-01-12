from django.db import models

# Create your models here.

class Review(models.Model):

    # name = models.CharField(max_length=254)
    review = models.TextField()
    rating = models.IntegerField(default=1,
                                 choices=((i, i) for i in range(1, 6)))
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name