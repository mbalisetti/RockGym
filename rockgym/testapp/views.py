from django.shortcuts import render,redirect
from testapp.forms import Signupform
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
	return render(request,'testapp/home.html')


def signup_view(request):
	form=Signupform()
	if request.method=='POST':
		form=Signupform(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return redirect('/accounts/login')
	return render(request,'testapp/signup.html',{'form':form})


@login_required
def equp_view(request):
	return render(request,'testapp/equipments.html')

@login_required
def trainer_view(request):
	return render(request,'testapp/trainer.html')

@login_required
def fee_view(request):
	return render(request,'testapp/fee.html')

@login_required
def sched_view(request):
	return render(request,'testapp/sched.html')



def add_view(request):
	return render(request,'testapp/add.html')