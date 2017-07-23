from django.shortcuts import render, redirect
from .models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import EatForm, WorkoutForm
# Create your views here.

def index(request): 
	form = AuthenticationForm
	return render(request,'cal/index.html',{'form':form})



def test(request):
	user = request.user
	profile = user.profile
	name = profile.name
	gender = profile.gender


	print(request.user)
	return render(request,'cal/test.html',{})

@login_required
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

	eats = Eat.objects.filter(user_id=user.pk).order_by('-date')[:10]
	workouts = Workout.objects.filter(user_id=user.pk).order_by('-date')[:10]

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	eats_today = Eat.objects.filter(user_id=user.pk, date__range=(today_min, today_max))
	workouts_today = Workout.objects.filter(user_id=user.pk, date__range=(today_min, today_max))
	# eats_today = Eat.objects.filter(user_id=user.pk).order_by('date')[:10]
	eat_sum = 0
	for eat in eats_today:
		eat_sum += eat.food.calorie * eat.amount

	workout_sum = 0
	for workout in workouts_today:
		workout_sum += workout.exercise.calorie * workout.duration
	
	left_calorie = int(eat_sum - BMR - workout_sum)

	context = {
		"profile":profile,
		"eats": eats,
		"workouts": workouts,
		"workouts_today": workouts_today,
		"eats_today": eats_today,
		"eat_sum": eat_sum,
		"workout_sum": workout_sum,
		"left_calorie": left_calorie,
			}

	return render(request,'cal/mypage.html',context)

@login_required
def new_workout(request):
    if request.method == "POST":
        workoutform = WorkoutForm(request.POST)
        if workoutform.is_valid:
            workout= workoutform.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect(mypage)
    else:
        workoutform = WorkoutForm
    return render(request,'cal/new_workout.html',{'form':workoutform})


@login_required
def new_eat(request):
    if request.method == "POST":
        eatform = EatForm(request.POST)
        if eatform.is_valid:
            eat= eatform.save(commit=False)
            eat.user = request.user
            eat.save()
            return redirect(mypage)
    else:
        eatform = EatForm
    return render(request,'cal/new_eat.html',{'form':eatform})
