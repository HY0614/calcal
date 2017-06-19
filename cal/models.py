from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
	name = models.CharField(max_length=10)
	age = models.IntegerField()
	weight = models.IntegerField()
	height = models.IntegerField()
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	gender = models.IntegerField(choices=((1,("male")), (2,("female"))),default = 1)
	bmr = models.IntegerField(blank=True) #보이지 않게 하자
	def __str__(self):
		return str(self.name)

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
	duration = models.FloatField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user) + "exercise" + self.exercise.name



