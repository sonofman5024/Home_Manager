from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegisterForm
from .models import User, Kid
import datetime

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_parent = True
            user.save()
            return redirect("thank_you")
        else: 
        
            return HttpResponse("registration failed")
           


    else:
        return render(request, "register.html", {'register_form':RegisterForm})

def pre_register(request):
    if request.method == 'POST':
        if request.POST['action']=='submit':
            email = request.POST['email']
            parent = User.objects.get(email=email)
            if parent:
                return render(request, "pre_register.html", {'parent':parent})  
            else:
                return HttpResponse("no such person!")
        elif request.POST['action']=='YES':
            print(request.POST['parent'])
            request.session['parent'] = request.POST['parent']
            return redirect('register_kid')  
          
    else:
        return render(request, "pre_register.html", )

def parent_conf(request):
    return render(request, 'parent_conf.html', )

def register_kid(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        parent = request.POST['parent']
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_kid = True
            user.save()
            Kid.objects.create(user = user, parent=User.objects.get(username=parent), reward_credit = 0)

        else: 
            print("wrong")
        return redirect("thank_you")   


    else:
        return render(request, "register_kid.html", {'register_form':RegisterForm})

def thank_you(request):
    return render(request, "thank_you_regi.html", context = None)

def fork(request):
    return render(request, "fork.html", context = None)

