from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
