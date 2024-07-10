from django.db import models


class StudentComplain(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name

class StudentProposal(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=18)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return self.first_name


