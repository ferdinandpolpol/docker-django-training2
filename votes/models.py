from django.db import models

# Create your models here.
class Position(models.Model):
    description = models.CharField(max_length=50)
    position_power = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Candidate(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + ", " + self.first_name