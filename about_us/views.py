from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_us(request):
    my_dict= {"insert_me" : "Im from first.py"}
    return render(request, "about_us/index.html", context= my_dict)
