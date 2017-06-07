from django.contrib import admin
from .models import Food,Eat,Exercise,Workout


class FoodAdmin(admin.ModelAdmin):
	list_display = ['name','calorie','category']

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ['name','calorie']
# Register your models here.
admin.site.register(Food,FoodAdmin)
admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Eat)
admin.site.register(Workout)
