from django.shortcuts import render

# Create your views here.
def rewards(request):
    
    return render(request, "rewards.html", context = None)