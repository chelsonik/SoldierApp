from django.db import models

# Create your models here.

class Soldier(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    reason =  models.TextField(max_length=100)
    platoon = models.IntegerField()

    def get_absolute_url(self):
        return f"/soldiers/{self.id}/"