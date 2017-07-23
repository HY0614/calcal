from django import forms
from .models import Workout,Eat
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise','duration']
class EatForm(forms.ModelForm):
    class Meta:
        model = Eat
        fields = ['food','amount']