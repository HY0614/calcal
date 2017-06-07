from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Food(models.Model):
	name = models.CharField(max_length=20)
	calorie = models.IntegerField()
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.name



class Exercise(models.Model):
	name = models.CharField(max_length=20)
	calorie = models.IntegerField()

	def __str__(self):
		return self.name

class Eat(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	food = models.ForeignKey(Food)
	amount = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user) + " ate "+ self.food.name

class Workout(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	exercise = models.ForeignKey(Exercise)
	duration = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user) + "exercise" + self.exercise.name
		


