from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Clubs(models.Model):
     club_name = models.CharField(max_length=64)
     league_name = models.CharField(max_length=64)
     trophies = models.TextField()
     purchaser =models.ForeignKey(CustomUser, on_delete = models.CASCADE)

     def __str__(self):
        return self.club_name

     def get_absolute_url(self):
        return reverse('clubs-list')