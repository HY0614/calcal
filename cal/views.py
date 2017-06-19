from django.shortcuts import render
from .models import *
# Create your views here.

def test(request):
	print(request.user)
	return render(request,'cal/test.html',{})


def mypage(request):
	user = request.user
	profile= user.profile

	#BMR 계산하는 부분
	if 1==profile.gender:
		BMR = int(66 + (13.8 * profile.weight) + (5 * profile.height) - (6.8 * profile.age))
	else:
		BMR = int(655 + (9.6 * profile.weight) + (1.8 * profile.height) - (4.7 * profile.age))

	profile.bmr = BMR
	profile.save()

	#최근 먹은 음식 및 운동현황

	eats = Eat.objects.filter(user_id)
	workouts = Workout.objects.all()

	context = {
		"profile":profile,
		"eats": eats,
		"workouts": workouts,
	}

	return render(request,'cal/test.html',context)
 

