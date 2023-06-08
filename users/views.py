from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegister
from django.contrib.auth import login , logout , authenticate
# Create your views here.

def register(request):
	if request.method=='POST':
		form=UserRegister(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			user=form.save()
			messages.success(request , f'account created for {username}!! You can now login..')
			#login(request,user)
			return redirect('login')
	else:
		form=UserRegister()

	return render(request,'users/register.html',context={'form':form})
