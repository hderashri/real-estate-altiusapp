from django.db import models

class Apartment(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
