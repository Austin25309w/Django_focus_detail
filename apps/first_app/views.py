from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
	
	return render(request,"login_reg.html")

def validate(request):
	# if request.method == "POST":
	errors = Guest.objects.reg_validator(request.POST)
	if len(errors):
		request.session['name'] =request.POST['name']
		request.session['username'] =request.POST['reg_username']
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		guest = Guest.objects.create()
		guest.name = request.POST['name']
		guest.username = request.POST['reg_username']
		guest.password =  bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())		

		guest.save()
		request.session['id'] = guest.id

		messages.success(request, "successfully registered! ")
       	
	return redirect('/dashboard')

def login(request):
	errors = Guest.objects.log_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		guest = Guest.objects.get(username = request.POST['log_username'])
		request.session['name'] = guest.name
		request.session['id'] = guest.id

		messages.success(request, "successfully registered! ")
		return redirect('/dashboard')



def dashboard(request):
	context = {"users" : Guest.objects.all()}		
	return render(request, "dashboard.html", context)


def add(request):
	if request.method == "POST":
		item = Item.objects.create()
		item.name =request.POST['item_name']
		item.save()
	return redirect("/process")

def process(request):
	return render(request, 'show.html')



def delete(request, id):
	deleteuser =Guest.objects.get(id=id)
	deleteuser.delete()
	return redirect('/dashboard')


# def show(request, id):
# 	show = Guest.objects.get(id=id)
# 	user = {
# 		"id" : show.id,
# 		"username" : show.username,
# 		"date" : show.created_at
# 		}
# 	return render(request, "show.html", user)

def logout(request):
	request.session.clear()
	return redirect('/')