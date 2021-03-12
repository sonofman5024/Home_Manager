from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            form.save()
        else: 
            print("wrong")
        return redirect("thank_you.html")


    else:
        return render(request, "register.html", {'register_form':RegisterForm})

def thank_you(request):
    return render(request, "thank_you_regi.html", context = None)

def fork(request):
    return render(request, "fork.html", context = None)

