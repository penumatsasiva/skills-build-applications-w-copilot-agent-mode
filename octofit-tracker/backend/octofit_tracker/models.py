from djongo import models
from django.contrib.auth.models import AbstractUser

# Custom user model (if needed)
class User(AbstractUser):
	email = models.EmailField(unique=True)
	team = models.CharField(max_length=50, blank=True, null=True)

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.JSONField(default=list)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.CharField(max_length=100)
	activity = models.CharField(max_length=100)
	distance = models.FloatField()
	def __str__(self):
		return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
	team = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.team}: {self.points}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name
