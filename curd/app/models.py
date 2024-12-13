from django.db import models


class Student(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  email = models.EmailField()
  age = models.IntegerField()
  gender = models.CharField(max_length=120)
  
  def __str__(self):
    return self.name
