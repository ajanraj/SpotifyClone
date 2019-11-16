from django.db import models

# Create your models here.


class Moods(models.Model):

    moods_name = models.CharField(max_length=50)
    moods_des = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.moods_name
