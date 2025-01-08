from django.db import models

# Create your models here.

class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio"

    name = models.CharField(max_length=254)
    website_url = models.URLField(max_length=1250, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name